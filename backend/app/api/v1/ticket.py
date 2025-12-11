from fastapi import APIRouter, HTTPException
from typing import List
from app.core.db import get_connection
from app.schemas.ticket import TicketCreate, TicketUpdate, TicketResponse

router = APIRouter(tags=["Tickets"])


# GET ALL TICKETS
@router.get("/tickets", response_model=List[TicketResponse])
def get_tickets():
    conn = get_connection()
    cursor = conn.cursor()
    rows = cursor.execute("SELECT * FROM tickets").fetchall()
    conn.close()
    return [dict(row) for row in rows]


# GET TICKET BY ID
@router.get("/tickets/{ticket_id}", response_model=TicketResponse)
def get_ticket(ticket_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    row = cursor.execute(
        "SELECT * FROM tickets WHERE id = ?", (ticket_id,)
    ).fetchone()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return dict(row)


# CREATE TICKET
@router.post("/tickets", response_model=TicketResponse)
def create_ticket(ticket: TicketCreate):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO tickets (title, description, status, priority)
        VALUES (?, ?, ?, ?)
        """,
        (ticket.title, ticket.description, ticket.status, ticket.priority)
    )

    conn.commit()
    new_id = cursor.lastrowid
    conn.close()

    return {
        "id": new_id,
        **ticket.dict(),
    }


# UPDATE TICKET
@router.put("/tickets/{ticket_id}", response_model=TicketResponse)
def update_ticket(ticket_id: int, ticket: TicketUpdate):
    conn = get_connection()
    cursor = conn.cursor()

    # Check exists
    existing = cursor.execute(
        "SELECT * FROM tickets WHERE id = ?", (ticket_id,)
    ).fetchone()

    if not existing:
        conn.close()
        raise HTTPException(status_code=404, detail="Ticket not found")

    cursor.execute(
        """
        UPDATE tickets
        SET title = COALESCE(?, title),
            description = COALESCE(?, description),
            status = COALESCE(?, status),
            priority = COALESCE(?, priority),
            updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
        """,
        (ticket.title, ticket.description, ticket.status, ticket.priority, ticket_id)
    )

    conn.commit()

    updated = cursor.execute(
        "SELECT * FROM tickets WHERE id = ?", (ticket_id,)
    ).fetchone()

    conn.close()

    return dict(updated)


# DELETE TICKET
@router.delete("/tickets/{ticket_id}")
def delete_ticket(ticket_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    # Verify exists
    row = cursor.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,)).fetchone()
    if not row:
        conn.close()
        raise HTTPException(status_code=404, detail="Ticket not found")

    cursor.execute("DELETE FROM tickets WHERE id = ?", (ticket_id,))
    conn.commit()
    conn.close()

    return {"message": "Ticket deleted"}

from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query
from app.core.db import get_connection
from app.schemas.ticket import TicketCreate, TicketUpdate, TicketResponse

router = APIRouter(prefix="/tickets", tags=["Tickets"])



# GET ALL TICKETS
@router.get("", response_model=List[TicketResponse])
def list_tickets(
    status: Optional[str] = Query(None),
    priority: Optional[str] = Query(None),
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
):
    conn = get_connection()

    query = "SELECT * FROM tickets WHERE 1=1"
    params = []

    if status:
        query += " AND status = ?"
        params.append(status)

    if priority:
        query += " AND priority = ?"
        params.append(priority)

    query += " ORDER BY created_at DESC LIMIT ? OFFSET ?"
    params.extend([limit, offset])

    rows = conn.execute(query, params).fetchall()
    conn.close()

    return [
        TicketResponse(
            id=row["id"],
            title=row["title"],
            description=row["description"],
            status=row["status"],
            priority=row["priority"],
        )
        for row in rows
    ]

# GET TICKET BY ID
@router.get("/{ticket_id}", response_model=TicketResponse)
def get_ticket(ticket_id: int):
    conn = get_connection()
    row = conn.execute(
        "SELECT * FROM tickets WHERE id = ?", (ticket_id,)
    ).fetchone()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return TicketResponse(
        id=row["id"],
        title=row["title"],
        description=row["description"],
        status=row["status"],
        priority=row["priority"],
    )


# CREATE TICKET
@router.post("", response_model=TicketResponse)
def create_ticket(ticket: TicketCreate):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO tickets (title, description, status, priority)
        VALUES (?, ?, ?, ?)
        """,
        (
            ticket.title,
            ticket.description,
            ticket.status.value,
            ticket.priority.value,
        ),
    )

    conn.commit()
    ticket_id = cursor.lastrowid

    row = cursor.execute(
        "SELECT * FROM tickets WHERE id = ?", (ticket_id,)
    ).fetchone()

    conn.close()

    return TicketResponse(
        id=row["id"],
        title=row["title"],
        description=row["description"],
        status=row["status"],
        priority=row["priority"],
    )


# UPDATE TICKET
@router.put("/{ticket_id}", response_model=TicketResponse)
def update_ticket(ticket_id: int, ticket: TicketUpdate):
    conn = get_connection()
    cursor = conn.cursor()

    existing = cursor.execute(
        "SELECT id FROM tickets WHERE id = ?", (ticket_id,)
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
        (
            ticket.title,
            ticket.description,
            ticket.status.value if ticket.status else None,
            ticket.priority.value if ticket.priority else None,
            ticket_id,
        ),
    )

    conn.commit()

    row = cursor.execute(
        "SELECT * FROM tickets WHERE id = ?", (ticket_id,)
    ).fetchone()

    conn.close()

    return TicketResponse(
        id=row["id"],
        title=row["title"],
        description=row["description"],
        status=row["status"],
        priority=row["priority"],
    )


# DELETE TICKET
@router.delete("/{ticket_id}")
def delete_ticket(ticket_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    row = cursor.execute(
        "SELECT id FROM tickets WHERE id = ?", (ticket_id,)
    ).fetchone()

    if not row:
        conn.close()
        raise HTTPException(status_code=404, detail="Ticket not found")

    cursor.execute("DELETE FROM tickets WHERE id = ?", (ticket_id,))
    conn.commit()
    conn.close()

    return {"message": "Ticket deleted"}

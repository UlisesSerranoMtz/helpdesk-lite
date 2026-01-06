from typing import Optional
from app.core.db import get_connection


def fetch_tickets(
    status: str,
    priority: str,
    limit: int,
    offset: int,
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
    return rows


def fetch_ticket_by_id(ticket_id: int):
    conn = get_connection()
    row = conn.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,)).fetchone()
    conn.close()

    return row


def insert_ticket(title: str, description: str, status: str, priority: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO tickets (title, description, status, priority)
        VALUES (?, ?, ?, ?)
        """,
        (
            title,
            description,
            status,
            priority,
        ),
    )

    conn.commit()
    ticket_id = cursor.lastrowid

    row = cursor.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,)).fetchone()

    conn.close()

    return row


def update_ticket_by_id(
    ticket_id: int,
    title: Optional[str],
    description: Optional[str],
    status: Optional[str],
    priority: Optional[str],
):
    conn = get_connection()
    cursor = conn.cursor()

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
            title,
            description,
            status,
            priority,
            ticket_id,
        ),
    )

    conn.commit()

    row = cursor.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,)).fetchone()

    conn.close()
    return row


def delete_ticket_by_id(ticket_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tickets WHERE id = ?", (ticket_id,))
    conn.commit()
    conn.close()

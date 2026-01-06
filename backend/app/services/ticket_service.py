from typing import List, Optional
from fastapi import HTTPException


from app.schemas.ticket import (
    TicketCreate,
    TicketUpdate,
    TicketResponse,
    StatusEnum,
    PriorityEnum
)

from app.repositories.ticket_repository import (
    fetch_tickets,
    fetch_ticket_by_id,
    insert_ticket,
    update_ticket_by_id,
    delete_ticket_by_id
)

def list_tickets_service (
    status: Optional[StatusEnum],
    priority: Optional[PriorityEnum],
    limit: int,
    offset: int,
) -> List[TicketResponse]:
    rows = fetch_tickets(
        status=status.value if status else None,
        priority=priority.value if priority else None,
        limit=limit,
        offset=offset
    )

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

def get_ticket_service(ticket_id: int) -> TicketResponse:
    row = fetch_ticket_by_id(ticket_id)
    if not row:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return TicketResponse(
        id=row["id"],
        title=row["title"],
        description=row["description"],
        status=row["status"],
        priority=row["priority"],
    )

def create_ticket_service(ticket: TicketCreate) -> TicketResponse:
    row = insert_ticket(
        title=ticket.title,
        description=ticket.description,
        status=ticket.status.value,
        priority=ticket.priority.value
    )

    return TicketResponse(
        id=row["id"],
        title=row["title"],
        description=row["description"],
        status=row["status"],
        priority=row["priority"],
    )

def update_ticket_service(
    ticket_id: int,
    ticket: TicketUpdate,
) -> TicketResponse:
    existing = fetch_ticket_by_id(ticket_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Ticket not found")

    row = update_ticket_by_id(
        ticket_id=ticket_id,
        title=ticket.title,
        description=ticket.description,
        status=ticket.status.value if ticket.status else None,
        priority=ticket.priority.value if ticket.priority else None
    )

    return TicketResponse(
        id=row["id"],
        title=row["title"],
        description=row["description"],
        status=row["status"],
        priority=row["priority"],
    )

def delete_ticket_service(ticket_id: int):
    existing = fetch_ticket_by_id(ticket_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Tciket not found")

    
    delete_ticket_by_id(ticket_id)
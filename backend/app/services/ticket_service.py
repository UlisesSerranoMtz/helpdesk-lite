from typing import List, Optional
from fastapi import HTTPException
from app.core.logger import logger


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
    logger.info(
        "Listing tickets | status=%s priority=%s limit=%s offset=%s",
        status.value if status else None,
        priority.value if priority else None,
        limit,
        offset
    )
    rows = fetch_tickets(
        status=status.value if status else None,
        priority=priority.value if priority else None,
        limit=limit,
        offset=offset
    )
    logger.info(
        "Tickets fetched from service | count=%s",
        len(rows)
        )

    return [
        TicketResponse(
            id=row["id"],
            title=row["title"],
            description=row["description"],
            status=StatusEnum(row["status"]),
            priority=PriorityEnum(row["priority"]),
        )
        for row in rows
    ]

def get_ticket_service(ticket_id: int) -> TicketResponse:
    logger.info(
        "Getting ticket by id | ticket_id=%s",
        ticket_id
    )
    row = fetch_ticket_by_id(ticket_id)
    if not row:
        logger.warning(
            "Ticket not found | ticket_id=%s",
            ticket_id
        )
        raise HTTPException(status_code=404, detail="Ticket not found")
    logger.info(
        "Ticket found | ticket_id=%s",
        ticket_id
    )

    return TicketResponse(
        id=row["id"],
        title=row["title"],
        description=row["description"],
        status=StatusEnum(row["status"]),
        priority=PriorityEnum(row["priority"]),
    )

def create_ticket_service(ticket: TicketCreate) -> TicketResponse:
    logger.info(
        "Creating Ticket | title=%s description=%s status=%s priority=%s",
        ticket.title,
        ticket.description,
        ticket.status.value,
        ticket.priority.value
    )
    row = insert_ticket(
        title=ticket.title,
        description=ticket.description,
        status=ticket.status.value,
        priority=ticket.priority.value
    )
    logger.info(
        "Ticket created successfully | ticket_id=%s",
        row["id"]
    )
    return TicketResponse(
        id=row["id"],
        title=row["title"],
        description=row["description"],
        status=StatusEnum(row["status"]),
        priority=PriorityEnum(row["priority"]),
    )

def update_ticket_service(
    ticket_id: int,
    ticket: TicketUpdate,
) -> TicketResponse:
    logger.info(
        "Updating ticket | ticket_id=%s",
        ticket_id
    )
    existing = fetch_ticket_by_id(ticket_id)
    if not existing:
        logger.warning(
            "Ticket not found for update | ticket_id=%s",
            ticket_id
        )
        raise HTTPException(status_code=404, detail="Ticket not found")

    row = update_ticket_by_id(
        ticket_id=ticket_id,
        title=ticket.title,
        description=ticket.description,
        status=ticket.status.value if ticket.status else None,
        priority=ticket.priority.value if ticket.priority else None
    )
    logger.info(
        "Ticket updated successfully | ticket_id=%s",
        ticket_id
    )
    return TicketResponse(
        id=row["id"],
        title=row["title"],
        description=row["description"],
        status=StatusEnum(row["status"]),
        priority=PriorityEnum(row["priority"]),
    )

def delete_ticket_service(ticket_id: int):
    logger.info(
        "Deleting ticket | ticket_id=%s",
        ticket_id
    )
    existing = fetch_ticket_by_id(ticket_id)
    if not existing:
        logger.warning(
            "Ticket not found for delete | ticket_id=%s",
            ticket_id
        )
        raise HTTPException(status_code=404, detail="Ticket not found")
 
    delete_ticket_by_id(ticket_id)

    logger.info(
        "Ticket deleted succesfully | ticket_id=%s",
        ticket_id
    )
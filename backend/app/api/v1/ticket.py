from typing import List, Optional
from fastapi import APIRouter, Query
from app.schemas.ticket import (
    TicketCreate,
    TicketUpdate,
    TicketResponse,
    StatusEnum,
    PriorityEnum,
)
from app.services.ticket_service import (
    list_tickets_service,
    get_ticket_service,
    create_ticket_service,
    update_ticket_service,
    delete_ticket_service
)

router = APIRouter(prefix="/tickets", tags=["Tickets"])


# GET ALL TICKETS
@router.get("", response_model=List[TicketResponse])
def list_tickets(
    status: Optional[StatusEnum] = Query(None),
    priority: Optional[PriorityEnum] = Query(None),
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
):
    return list_tickets_service(
        status=status,
        priority=priority,
        limit=limit,
        offset=offset
    )


# GET TICKET BY ID
@router.get("/{ticket_id}", response_model=TicketResponse)
def get_ticket(ticket_id: int):
    return get_ticket_service(ticket_id)


# CREATE TICKET
@router.post("", response_model=TicketResponse)
def create_ticket(ticket: TicketCreate):
    return create_ticket_service(ticket)
# UPDATE TICKET
@router.put("/{ticket_id}", response_model=TicketResponse)
def update_ticket(ticket_id: int, ticket: TicketUpdate):
    return update_ticket_service(ticket_id, ticket)


# DELETE TICKET
@router.delete("/{ticket_id}")
def delete_ticket(ticket_id: int):
    delete_ticket_service(ticket_id)
    return {"message": "ticket deleted"}
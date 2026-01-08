from typing import Optional, Dict, Any, List
from peewee import DoesNotExist, IntegrityError
from app.models.ticket import Ticket
from app.core.db import db


def fetch_tickets(
    status: Optional[str],
    priority: Optional[str],
    limit: int,
    offset: int,
) -> List[Dict[str, Any]]:
    query = Ticket.select()

    if status:
        query = query.where(Ticket.status == status)
    if priority:
        query = query.where(Ticket.priority == priority)
    
    return list(
        query
        .limit(limit)
        .offset(offset)
        .dicts()
    )


def fetch_ticket_by_id(ticket_id: int) -> Optional[Dict[str, Any]]:
    try:
        return Ticket.get_by_id(ticket_id).__data__
    except DoesNotExist:
        return None



def insert_ticket(
    title: str,
    description: str,
    status: str,
    priority: str
) -> Dict[str, Any]:
    with db.atomic():
        try:
            ticket = Ticket.create(
                title=title,
                description=description,
                status=status,
                priority=priority
            )
            return ticket.__data__
        except IntegrityError:
            ticket = Ticket.get(
                (Ticket.title == title) &
                (Ticket.status == status)
            )
            return ticket.__data__




def update_ticket_by_id(
    ticket_id: int,
    **data
):
    with db.atomic():
        Ticket.update(**data).where(Ticket.id == ticket_id).execute()
        return Ticket.get_by_id(ticket_id).__data__


def delete_ticket_by_id(ticket_id: int):
    Ticket.delete_by_id(ticket_id)

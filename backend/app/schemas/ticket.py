from pydantic import BaseModel
from enum import Enum


class StatusEnum(str, Enum):
    open = "open"
    in_progress = "in_progress"
    resolved = "resolved"


class PriorityEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class TicketBase(BaseModel):
    title: str
    description: str | None = None
    status: StatusEnum = StatusEnum.open
    priority: PriorityEnum = PriorityEnum.medium


class TicketCreate(TicketBase):
    pass


class TicketUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: StatusEnum | None = None
    priority: PriorityEnum | None = None


class TicketResponse(TicketBase):
    id: int

    class Config:
        from_attributes = True

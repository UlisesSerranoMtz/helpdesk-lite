from peewee import AutoField, CharField, TextField
from app.models.base import BaseModel

class Ticket(BaseModel):
    id = AutoField()
    title = CharField()
    description = TextField()
    status = CharField()
    priority = CharField()

    class Meta:
        indexes = {
            (("title", "status"), True)
        }
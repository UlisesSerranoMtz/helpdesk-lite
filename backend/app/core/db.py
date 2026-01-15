from peewee import SqliteDatabase
from app.core.config import DB_PATH
from app.models.base import database_proxy


db=SqliteDatabase(
    DB_PATH,
    pragmas={
        "journal_mode": "wal",
        "foreign_keys": 1
    }
)
def init_db():
    database_proxy.initialize(db)

    from app.models.ticket import Ticket
    db.create_tables([Ticket], safe=True)
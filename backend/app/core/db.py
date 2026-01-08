from peewee import SqliteDatabase
from pathlib import Path
from app.core.config import DB_PATH

db=SqliteDatabase(
    DB_PATH,
    pragmas={
        "journal_mode": "wal",
        "foreign_keys": 1
    }
)
def init_db():
    if db.is_closed():
        db.connect(reuse_if_open=True)
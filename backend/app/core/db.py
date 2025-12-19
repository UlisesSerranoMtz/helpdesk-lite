import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent.parent / "helpdesk.db"

print("DB PATH:", DB_PATH)

def get_connection():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    schema_path = Path(__file__).resolve().parent.parent / "db" / "schema.sql"
    with open(schema_path, "r") as f:
        cursor.executescript(f.read())

    conn.commit()
    conn.close()

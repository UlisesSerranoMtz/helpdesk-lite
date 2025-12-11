import sqlite3
from pathlib import Path
DB_PATH = Path(__file__).resolve().parent.parent.parent / "helpdesk.db"


def get_connection():
    """Obtiene conexión a la base de datos"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    schema_path = Path(__file__).resolve().parent.parent / "db"/"schema.sql"
    with open(schema_path, "r") as f:
        schema_sql = f.read()

    cursor.executescript(schema_sql)
    conn.commit()
    conn.close()

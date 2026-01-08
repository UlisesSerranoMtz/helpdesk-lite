import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = os.getenv("DB_PATH", BASE_DIR / "helpdesk.db")
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(',')
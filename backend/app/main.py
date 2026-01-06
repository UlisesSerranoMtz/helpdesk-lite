from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.db import init_db
from app.api.v1.ticket import router as ticket_router
from app.core.config import CORS_ORIGINS

app = FastAPI(title="Helpdesk API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "DELETE", "POST", "PUT", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"]
)
@app.on_event("startup")
def startup():
    init_db()

@app.get("/health")
def health():
    return {"status": "ok", "service": "helpdesk-api"}

# 🔹 Rutas
app.include_router(ticket_router, prefix="/api/v1")

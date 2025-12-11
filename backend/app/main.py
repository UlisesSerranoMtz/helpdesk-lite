from fastapi import FastAPI
from app.core.db import init_db
from app.api.v1.ticket import router as ticket_router

app = FastAPI(title="Helpdesk API")

init_db()
@app.get("/health")
def health():
    return {"status": "ok", "service": "helpdesk-api"}


app.include_router(ticket_router, prefix="/api/v1")

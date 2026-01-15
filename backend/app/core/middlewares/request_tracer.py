import time
from fastapi import Request
from app.core.db import db
from app.core.logger import logger

async def request_tracer_middleware(request: Request, call_next):
    start_time = time.time()
    response = None
    
    if db.is_closed():
        db.connect(reuse_if_open=True)

    try:
        response = await call_next(request)
        return response
    
    finally:
        duration_ms = round((time.time() - start_time) * 1000, 2)

        logger.info(
            "Request completed",
            extra={
                "method": request.method,
                "path": request.url.path,
                "status_code": response.status_code,
                "duration": duration_ms
            }
        )
        if not db.is_closed():
            db.close()
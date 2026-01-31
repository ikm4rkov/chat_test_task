from fastapi import FastAPI
import time
from fastapi import Request
from chat_test_task.core.logging import logger
from chat_test_task.api.chats import router as chats_router


app = FastAPI(
    title="Chat Test Task API",
    version="1.0.0",
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time

    logger.info(
        "%s %s - %s (%.3f sec)",
        request.method,
        request.url.path,
        response.status_code,
        process_time,
    )

    return response

app.include_router(chats_router, prefix="/chats", tags=["chats"])

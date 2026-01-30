from fastapi import FastAPI

from chat_test_task.api.chats import router as chats_router


app = FastAPI(
    title="Chat Test Task API",
    version="1.0.0",
)

app.include_router(chats_router, prefix="/chats", tags=["chats"])

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from chat_test_task.dependencies.db import get_db
from chat_test_task.schemas.chat import ChatCreate, ChatRead
from chat_test_task.schemas.message import MessageCreate, MessageRead
from chat_test_task.crud.chat import create_chat, get_chat, delete_chat
from chat_test_task.crud.message import create_message, get_last_messages


router = APIRouter()


@router.post("/", response_model=ChatRead, status_code=status.HTTP_201_CREATED)
def create_chat_endpoint(
    payload: ChatCreate,
    db: Session = Depends(get_db),
):
    chat = create_chat(db, payload.title)
    return ChatRead(
        id=chat.id,
        title=chat.title,
        created_at=chat.created_at,
        messages=[],
    )


@router.post("/{chat_id}/messages/", response_model=MessageRead)
def send_message_endpoint(
    chat_id: int,
    payload: MessageCreate,
    db: Session = Depends(get_db),
):
    chat = get_chat(db, chat_id)
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")

    return create_message(db, chat_id, payload.text)


@router.get("/{chat_id}", response_model=ChatRead)
def get_chat_endpoint(
    chat_id: int,
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    chat = get_chat(db, chat_id)
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")

    messages = get_last_messages(db, chat_id, limit)
    return ChatRead(
        id=chat.id,
        title=chat.title,
        created_at=chat.created_at,
        messages=messages,
    )


@router.delete("/{chat_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_chat_endpoint(
    chat_id: int,
    db: Session = Depends(get_db),
):
    chat = get_chat(db, chat_id)
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")

    delete_chat(db, chat)

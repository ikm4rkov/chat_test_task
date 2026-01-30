from sqlalchemy.orm import Session
from sqlalchemy import select, desc

from chat_test_task.models.message import Message


def create_message(db: Session, chat_id: int, text: str) -> Message:
    message = Message(chat_id=chat_id, text=text)
    db.add(message)
    db.commit()
    db.refresh(message)
    return message


def get_last_messages(
    db: Session,
    chat_id: int,
    limit: int,
) -> list[Message]:
    stmt = (
        select(Message)
        .where(Message.chat_id == chat_id)
        .order_by(desc(Message.created_at))
        .limit(limit)
    )
    return list(reversed(db.scalars(stmt).all()))

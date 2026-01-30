from sqlalchemy.orm import Session

from chat_test_task.models.chat import Chat


def create_chat(db: Session, title: str) -> Chat:
    chat = Chat(title=title)
    db.add(chat)
    db.commit()
    db.refresh(chat)
    return chat


def get_chat(db: Session, chat_id: int) -> Chat | None:
    return db.get(Chat, chat_id)


def delete_chat(db: Session, chat: Chat) -> None:
    db.delete(chat)
    db.commit()

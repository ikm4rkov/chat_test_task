from datetime import datetime
from typing import List

from pydantic import BaseModel, constr

from chat_test_task.schemas.message import MessageRead


class ChatCreate(BaseModel):
    title: constr(min_length=1, max_length=200)

    def model_post_init(self, __context):
        self.title = self.title.strip()


class ChatRead(BaseModel):
    id: int
    title: str
    created_at: datetime
    messages: List[MessageRead]

    model_config = {"from_attributes": True}

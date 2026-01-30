from datetime import datetime

from pydantic import BaseModel, constr


class MessageCreate(BaseModel):
    text: constr(min_length=1, max_length=5000)

    def model_post_init(self, __context):
        self.text = self.text.strip()


class MessageRead(BaseModel):
    id: int
    chat_id: int
    text: str
    created_at: datetime

    model_config = {"from_attributes": True}

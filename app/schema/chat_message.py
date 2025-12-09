from pydantic import BaseModel
from datetime import datetime

class ChatMessageCreate(BaseModel):
    sender_id: int
    receiver_id: int
    message: str

class ChatMessageResponse(BaseModel):
    id: int
    sender_id: int
    receiver_id: int
    message: str
    timestamp: datetime

    class Config:
        orm_mode = True

# app/router/chat_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.db_configuration import get_db
from app.model.user import User
from app.model.chat_message import ChatMessage
from app.schema.chat_message import ChatMessageCreate, ChatMessageResponse
from app.rabbitmq.publisher import publish_message

router = APIRouter()

# GET endpoint (already existing)
@router.get("/messages/{user_id}", response_model=list[ChatMessageResponse])
def get_messages(user_id: int, db: Session = Depends(get_db)):
    messages = db.query(ChatMessage).filter(
        (ChatMessage.sender_id == user_id) | (ChatMessage.receiver_id == user_id)
    ).all()
    return messages

# NEW: POST endpoint to send message from one user to another
@router.post("/messages/send", response_model=dict)
def send_message(msg: ChatMessageCreate, db: Session = Depends(get_db)):
    # Check if sender exists
    sender = db.query(User).filter(User.id == msg.sender_id).first()
    if not sender:
        raise HTTPException(status_code=404, detail="Sender not found")

    receiver = db.query(User).filter(User.id == msg.receiver_id).first()
    if not receiver:
        raise HTTPException(status_code=404, detail="Receiver not found")

    # Publish message to RabbitMQ
    publish_message(msg.sender_id, msg.receiver_id, msg.message)

    return {"message": "Message sent successfully"}

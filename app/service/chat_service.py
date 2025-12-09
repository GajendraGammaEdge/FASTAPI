# app/service/chat_service.py
from app.db.db_configuration import get_db
from app.model.chat_message import ChatMessage
from app.model.user import User
from sqlalchemy.orm import Session

def save_chat_message_to_db(data: dict):
    db: Session = next(get_db())
    # Optionally, validate sender and receiver exist
    sender = db.query(User).filter(User.id == data['sender_id']).first()
    receiver = db.query(User).filter(User.id == data['receiver_id']).first()
    if not sender or not receiver:
        print("Invalid sender or receiver")
        return

    chat_message = ChatMessage(
        sender_id=data['sender_id'],
        receiver_id=data['receiver_id'],
        message=data['message']
    )
    db.add(chat_message)
    db.commit()
    db.refresh(chat_message)
    return chat_message
# app/service/chat_service.py
from app.db.db_configuration import get_db
from app.model.chat_message import ChatMessage
from app.model.user import User
from sqlalchemy.orm import Session

def save_chat_message_to_db(data: dict):
    db: Session = next(get_db())
    # Optionally, validate sender and receiver exist
    sender = db.query(User).filter(User.id == data['sender_id']).first()
    receiver = db.query(User).filter(User.id == data['receiver_id']).first()
    if not sender or not receiver:
        print("Invalid sender or receiver")
        return

    chat_message = ChatMessage(
        sender_id=data['sender_id'],
        receiver_id=data['receiver_id'],
        message=data['message']
    )
    db.add(chat_message)
    db.commit()
    db.refresh(chat_message)
    return chat_message

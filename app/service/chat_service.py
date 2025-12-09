from app.model.chat_message import ChatMessage
from app.model.user import User
from sqlalchemy.orm import Session

def save_chat_message_to_db(data, db: Session):
    # Access Pydantic model correctly
    sender = db.query(User).filter(User.id == data.sender_id).first()
    receiver = db.query(User).filter(User.id == data.receiver_id).first()

    if not sender or not receiver:
        raise ValueError("Sender or receiver does not exist")

    message = ChatMessage(
        sender_id=data.sender_id,
        receiver_id=data.receiver_id,
        message=data.message
    )

    db.add(message)
    db.commit()
    db.refresh(message)

    return message

from sqlalchemy import Column, Integer, String, Text, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship
from app.db.db_configuration import Base


class ChatSession(Base):
    __tablename__ = "chat_sessions"

    id = Column(Integer, primary_key=True, index=True)
    model = Column(String, index=True)
    max_tokens = Column(Integer, default=512)
    temperature = Column(Float, default=1.0)

    # relationship to messages
    messages = relationship("Message", back_populates="session", cascade="all, delete-orphan")


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("chat_sessions.id"))
    
    role = Column(String, index=True)            # system / user / assistant
    content = Column(Text)                       # message text content

    session = relationship("ChatSession", back_populates="messages")


class ChatGenerationLog(Base):
    __tablename__ = "chat_generation_log"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("chat_sessions.id"))
    model = Column(String)
    output_text = Column(Text)
    tokens_used = Column(Integer, nullable=True)
    finished = Column(Boolean, default=True)

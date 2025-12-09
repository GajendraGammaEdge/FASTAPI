from sqlalchemy import Column, ForeignKey, Integer, String ,DateTime
from sqlalchemy.orm import relationship
from app.db.db_configuration import Base
from app.model.user import User
from datetime import datetime

class UploadFiles(Base):
    __tablename__ = "upload_files"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    file_name = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    
    owner = relationship("User", back_populates="files")

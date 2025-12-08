from pydantic import Field
from typing import Optional
from app.db.db_configuration import Base
from sqlalchemy import Column,ForeignKey, Integer,String
from app.model.user import User
from sqlalchemy.orm import relationship

class UploadFiles(Base):
    __tablename__ = "upload_files"
    id = Column(Integer , primary_key=True , autoincrement=True)
    file_name = Column(String,nullable= True)
    file_path = Column(String, nullable= True)
    user_id = Column(Integer,ForeignKey("users.id"), nullable=False)
    
    owner = relationship("User", back_populates="files")
    
    
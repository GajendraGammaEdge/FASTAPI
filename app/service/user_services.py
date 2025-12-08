from fastapi import HTTPException
from app.model.user import User  
from sqlalchemy.orm import Session
from app.schema.user_schema import UserCreate
from typing import List

class UserServices():
    def __init__(self, db: Session):
        self.db = db 
    
    def get_user(self,user_id: int):
       return self.db.query(User).filter(User.id == user_id).first()
    
    def create_user(self, user_data: UserCreate):
        existing_user = self.db.query(User).filter(User.username == user_data.username).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already exists")
        
        new_user = User(**user_data.model_dump())
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        
        return new_user

    def get_users(self) -> List[User]:
        # Use 'self.db' to access the session
        return self.db.query(User).all()
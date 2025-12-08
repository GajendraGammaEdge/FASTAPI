from fastapi import APIRouter ,Depends
from app.service.user_services import UserServices # Ensure this path/case matches your file system
from app.db.db_configuration import get_db
from sqlalchemy.orm import Session
from app.schema.user_schema import UserCreate, UserRead
from typing import List 

router  = APIRouter()

@router.post("/create_user", response_model=UserRead) 
async def create_user(user : UserCreate , db: Session= Depends(get_db)):
    service = UserServices(db)
    return  service.create_user(user)  
    

@router.get("/users", response_model=List[UserRead])  
async def get_users(db: Session = Depends(get_db)): # Changed function name to plural
    service = UserServices(db)
    return service.get_users()
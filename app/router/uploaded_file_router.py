from sqlalchemy.orm import Session 
from app.db.db_configuration import get_db 
from app.service.upload_file_service import upload_file, get_user_files
from app.service.user_services import UserServices
from fastapi import HTTPException , APIRouter , Depends, UploadFile , File

router = APIRouter()

@router.post("uploading_file/{user_id}") 
async def uploading_file(user_id : int ,db:Session = Depends(get_db) ,  file : UploadFile = File(description="Uploaded the images and  pdf ")):
    user_services = UserServices(db)
    user = user_services.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User is not present with this user_id")
    
    content = await file.read()
    file.file = content 
    uploaded = upload_file(db, file, user)
    return {"message":"File is successfully uploaded","file_name":uploaded.file_name}


@router.get("getfile_user/{user_id}")
async def get_user_file(user_id:int , db :Session = Depends(get_db)):
    user_services = UserServices(db)
    user = user_services.get_user(user_id)
    if not user :
        raise HTTPException(status_code=404 , detail="User is not Found")
    
    files = get_user_files(db, user_id)
    return [{"file_id": f.id, "file_name": f.file_name, "file_path": f.file_path} for f in files]


 
    
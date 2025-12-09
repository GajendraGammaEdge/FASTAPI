from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.db.db_configuration import get_db
from app.service.upload_file_service import upload_file, get_user_files
from app.service.user_services import UserServices

router = APIRouter()

@router.post("/uploading_file/{user_id}")
async def uploading_file(
    user_id: int,
    db: Session = Depends(get_db),
    file: UploadFile = File(..., description="Upload images or PDFs")
):

    user_services = UserServices(db)
    user = user_services.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    uploaded = await upload_file(db, user, file)
    return {"message": "File successfully uploaded", "file_name": uploaded.file_name}


@router.get("/getfile_user/{user_id}")
def get_user_file(user_id: int, db: Session = Depends(get_db)):
    user_services = UserServices(db)
    user = user_services.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    files = get_user_files(db, user)
    return [{"file_id": f.id, "file_name": f.file_name, "file_path": f.file_path} for f in files]

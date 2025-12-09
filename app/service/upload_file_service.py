import os
from app.model.upload_files import UploadFiles
from sqlalchemy.orm import Session
from app.model.user import User
from dotenv import load_dotenv
load_dotenv()

UPLOAD_DIR = os.getenv("UPLOAD_FOLDER", "uploaded_file")
os.makedirs(UPLOAD_DIR, exist_ok=True)

async def save_file_to_disk(file: UploadFiles, filename: str):
    file_location = os.path.join(UPLOAD_DIR, filename)
    counter = 1
    while os.path.exists(file_location):
        name, ext = os.path.splitext(filename)
        file_location = os.path.join(UPLOAD_DIR, f"{name}_{counter}{ext}")
        counter += 1

    content = await file.read()
    with open(file_location, "wb") as f:
        f.write(content)
    return file_location

async def upload_file(db: Session, user: User, file: UploadFiles):
    file_location = await save_file_to_disk(file, file.filename)
    uploaded_file = UploadFiles(
        file_name=file.filename,
        file_path=file_location,
        user_id=user.id
    )
    db.add(uploaded_file)
    db.commit()
    db.refresh(uploaded_file)
    return uploaded_file

def get_user_files(db: Session, user: User):
    return db.query(UploadFiles).filter(UploadFiles.user_id == user.id).all()

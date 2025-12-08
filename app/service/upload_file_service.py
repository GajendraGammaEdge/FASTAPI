from app.model.upload_doc import UploadFiles
from app.schema.upload_file_schema import FileCreate ,FileResponse
from sqlalchemy.orm import Session
from app.model.user import User
import os
from dotenv import load_dotenv
load_dotenv()

Upload_dir  = os.getenv("UPLOAD_FOLDER")
os.makedirs("uploaded_file" , exist_ok= True)


def save_file_to_disk(file, filename: str):
    file_location = os.path.join(Upload_dir, filename)
    counter = 1
    while os.path.exists(file_location):
        name, ext  = os.path.splitext(filename)
        file_location = os.path.join(Upload_dir, f"{name}_{counter}{ext}")
        counter += 1
        
    with open(file_location, "wb") as f :
        content = file.read()
        f.write(content)
    return file_location

def upload_file(db : Session , user : User, file):
    file_location = save_file_to_disk(file , file.filename)
    upload_file = UploadFiles(file_name = file.filename, file_path = file_location, user_id = user.id)
    db.add(upload_file)
    db.commit()
    db.refresh(upload_file)
    return upload_file

def get_user_files(db: Session, user: User):
    return db.query(UploadFiles).filter(UploadFiles.user_id == user.id).all()
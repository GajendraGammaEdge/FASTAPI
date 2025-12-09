from fastapi import FastAPI, UploadFile, File
from typing import Annotated
from app.router.user_router import router as user_router 
from app.db.db_configuration import Base, engine  # make sure these are correct imports
from app.router.uploaded_file_router import router as file_router
from app.model import *
from app.router.chat_router import router as chat_router

app = FastAPI()

# include router correctly
app.include_router(file_router)
app.include_router(user_router)
app.include_router(chat_router)
Base.metadata.create_all(bind=engine)


@app.get("/health-check")
async def health_check():
    return {"status": "Application is working fine"}

if __name__ == "__main__":
    print("Run this app using: uvicorn main:app --reload")


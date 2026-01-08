from fastapi import FastAPI
from contextlib import asynccontextmanager
from dotenv import load_dotenv
import os
import tensorflow as tf

from app.router.user_router import router as user_router
from app.router.uploaded_file_router import router as file_router
from app.router.chat_router import router as chat_router
from app.router.image_processing import router as image_processing_router


# Load environment variables
load_dotenv()

MODEL_PATH = os.getenv("MODEL_PATH")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup 
    if not MODEL_PATH:
        raise RuntimeError("MODEL_PATH environment variable is not set")

    if not os.path.exists(MODEL_PATH):
        raise RuntimeError(f"Model file not found at: {MODEL_PATH}")

    app.state.model = tf.keras.models.load_model(MODEL_PATH)
    print("TensorFlow model loaded successfully")

    yield  

    # shutdowing the model 
    del app.state.model
    print("TensorFlow model unloaded")


# Create FastAPI app with lifespan
app = FastAPI(lifespan=lifespan)

# Include routers
app.include_router(file_router)
app.include_router(user_router)
app.include_router(chat_router)
app.include_router(image_processing_router)


@app.get("/health-check/")
async def health_check(
    name: str = "Gajendra",
    age: int = 23,
    department: str = "Python-developer"
):
    return {
        "status": "Application is working fine"
    }


if __name__ == "__main__":
    print("Run this app using: uvicorn app.main:app --reload")

from fastapi import APIRouter, UploadFile, File, Request
from app.utils.image_processing import preprocess_image
import io
from PIL import Image

router = APIRouter()


@router.post("/predict")
async def predict_image(
    request: Request,
    file: UploadFile = File(...)
):
    # Read image
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")

    # Preprocess
    processed_image = preprocess_image(image)

    # Get model from app state
    model = request.app.state.model

    # Predict
    predictions = model.predict(processed_image)[0]

    return {
        "brightness": float(predictions[0]),
        "contrast": float(predictions[1]),
        "saturation": float(predictions[2]),
        "sharpness": float(predictions[3]),
        "temperature": float(predictions[4]),
        "shadow": float(predictions[5])
    }

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origin = [
    'http://127.0.0.1:8000/docs#/'
]

app.add_middleware(
    CORSMiddleware,
    allow_origin= origin,
    allow_credential= origin,
    allow_methods = ["*"],
    allow_headers = ["*"]
)
import os
import socket
from dotenv import load_dotenv

from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return {
      "message": "Hello from FastAPI"
      }

@app.get("/health")
def health():
    return {
      "status": "ok"
      }

load_dotenv()
@app.get("/info")
def info():
    return {
      "hostname": socket.gethostname(),
      "app_env": os.getenv("APP_ENV", "dev")
      }


@app.get("/item/{item_id}")
def read_item(item_id: int):
    return {
      "item_id": item_id
      }

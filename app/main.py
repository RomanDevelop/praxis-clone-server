from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from app.engine import generate_engine_data
from app.alarms import check_and_create_alarms, get_all_alarms
from app.users import get_current_user, switch_user
import asyncio

app = FastAPI()

# Разрешаем Flutter-приложению подключаться (в будущем)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return "Ship Monitoring System 🚢"

@app.websocket("/ws/engine")
async def engine_socket(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = generate_engine_data()
            check_and_create_alarms(data)
            await websocket.send_json(data.model_dump())
            await asyncio.sleep(2)
    except Exception as e:
        print("WebSocket error:", e)

@app.get("/alarms")
def alarms():
    return get_all_alarms()

@app.get("/user")
def user():
    return get_current_user()

@app.post("/user/switch")
def switch(username: str):
    switch_user(username)
    return {"status": "switched", "username": username}

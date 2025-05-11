from fastapi import FastAPI, WebSocket, HTTPException, Depends, Query
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from datetime import datetime, timedelta
from typing import List, Optional
import asyncio
import jwt
from app.engine import generate_engine_data
from app.alarms import check_and_create_alarms, get_all_alarms, acknowledge_alarm
from app.models import EngineData, ErrorResponse, EngineLimits
from app.core.config import settings
from fastapi import WebSocketDisconnect

app = FastAPI(title="Ship Engine Monitoring System")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Rate limiting (add with slowapi or another library if needed)
# from fastapi.middleware.throttling import ThrottlingMiddleware
# app.add_middleware(
#     ThrottlingMiddleware,
#     rate_limit=settings.RATE_LIMIT_PER_MINUTE,
#     time_window=60
# )

# Error handling
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content=ErrorResponse(
            code="INTERNAL_ERROR",
            message=str(exc)
        ).model_dump()
    )

# Authentication
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except jwt.JWTError:
        raise HTTPException(
            status_code=401,
            detail=ErrorResponse(
                code="INVALID_TOKEN",
                message="Invalid authentication token"
            ).model_dump()
        )

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Implement your user authentication logic here
    if form_data.username != "admin" or form_data.password != "password":  # Replace with proper auth
        raise HTTPException(
            status_code=401,
            detail=ErrorResponse(
                code="INVALID_CREDENTIALS",
                message="Invalid username or password"
            ).model_dump()
        )
    access_token = create_access_token({"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}

# WebSocket endpoint for real-time engine data
@app.websocket("/engine/stream")
async def engine_stream(websocket: WebSocket):
    try:
        await websocket.accept()
        print("WebSocket connection accepted")
        
        while True:
            try:
                data = generate_engine_data()
                check_and_create_alarms(data)
                
                # Convert datetime to ISO format
                payload = data.model_dump()
                payload["timestamp"] = data.timestamp.isoformat()
                
                await websocket.send_json(payload)
                await asyncio.sleep(settings.WS_UPDATE_INTERVAL_MS / 1000)  # Convert ms to seconds
            except WebSocketDisconnect:
                print("WebSocket disconnected")
                break
            except Exception as e:
                print(f"Error in WebSocket loop: {e}")
                break
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        try:
            await websocket.close()
        except:
            pass

# REST API endpoints
@app.get("/api/engine/current", response_model=EngineData)
async def get_current_engine_data(current_user: dict = Depends(get_current_user)):
    """Get current engine parameters."""
    data = generate_engine_data()
    return data

@app.get("/api/engine/history")
async def get_engine_history(
    start_time: datetime = Query(...),
    end_time: datetime = Query(...),
    parameters: Optional[List[str]] = Query(None),
    current_user: dict = Depends(get_current_user)
):
    """Get historical engine data."""
    # Implement historical data retrieval logic here
    # This is a placeholder that returns current data
    data = generate_engine_data()
    return {"data": [data.model_dump()]}

@app.get("/api/engine/limits", response_model=EngineLimits)
async def get_engine_limits(current_user: dict = Depends(get_current_user)):
    """Get engine parameter limits."""
    return settings.ENGINE_LIMITS

@app.get("/api/alarms")
async def get_alarms(current_user: dict = Depends(get_current_user)):
    """Get all active alarms."""
    return get_all_alarms()

@app.post("/api/alarms/{alarm_id}/acknowledge")
async def acknowledge_alarm_endpoint(
    alarm_id: int,
    current_user: dict = Depends(get_current_user)
):
    """Acknowledge an alarm."""
    if acknowledge_alarm(alarm_id):
        return {"status": "success"}
    raise HTTPException(
        status_code=404,
        detail=ErrorResponse(
            code="ALARM_NOT_FOUND",
            message=f"Alarm with ID {alarm_id} not found"
        ).model_dump()
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )

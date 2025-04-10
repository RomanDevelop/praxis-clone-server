from pydantic import BaseModel
from datetime import datetime

class EngineData(BaseModel):
    rpm: int
    oil_temp: float
    coolant_temp: float
    fuel_pressure: float
    load: float
    timestamp: datetime


class Alarm(BaseModel):
    id: int
    message: str
    level: str  # "LOW", "MEDIUM", "HIGH"
    timestamp: datetime
    acknowledged: bool = False

class User(BaseModel):
    username: str
    role: str  # "engineer", "admin"


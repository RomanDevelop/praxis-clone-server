from datetime import datetime
from typing import List
from app.models import Alarm, EngineData

alarms: List[Alarm] = []

def check_and_create_alarms(data: EngineData) -> None:
    if data.oil_temp > 90.0:
        create_alarm("High oil temperature", "HIGH")
    if data.fuel_pressure < 2.5:
        create_alarm("Low fuel pressure", "MEDIUM")

def create_alarm(message: str, level: str) -> None:
    alarm = Alarm(
        id=len(alarms) + 1,
        message=message,
        level=level,
        timestamp=datetime.utcnow()
    )
    alarms.append(alarm)

def get_all_alarms() -> List[Alarm]:
    return alarms

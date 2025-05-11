from datetime import datetime
from typing import List, Dict
from app.models import Alarm, EngineData
from app.core.config import settings

alarms: List[Alarm] = []

def check_and_create_alarms(data: EngineData) -> None:
    """Check engine parameters against limits and create alarms if necessary."""
    limits = settings.ENGINE_LIMITS
    
    # Check each parameter against its limits
    for param_name, param_value in data.model_dump().items():
        if param_name == "timestamp" or param_name == "engine_hours":
            continue
            
        param_limits = getattr(limits, param_name, None)
        if not param_limits:
            continue
            
        # Check for critical condition
        if param_value >= param_limits.critical:
            create_alarm(param_name, f"Critical {param_name.replace('_', ' ')}: {param_value}", "CRITICAL")
        # Check for warning condition
        elif param_value >= param_limits.warning:
            create_alarm(param_name, f"Warning {param_name.replace('_', ' ')}: {param_value}", "WARNING")

def create_alarm(parameter: str, message: str, level: str) -> None:
    """Create a new alarm."""
    # Check if similar alarm already exists
    for alarm in alarms:
        if (alarm.parameter == parameter and 
            alarm.level == level and 
            not alarm.acknowledged):
            return
            
    alarm = Alarm(
        id=len(alarms) + 1,
        parameter=parameter,
        message=message,
        level=level,
        timestamp=datetime.utcnow()
    )
    alarms.append(alarm)

def get_all_alarms() -> List[Alarm]:
    """Get all active alarms."""
    return [alarm for alarm in alarms if not alarm.acknowledged]

def acknowledge_alarm(alarm_id: int) -> bool:
    """Acknowledge an alarm by its ID."""
    for alarm in alarms:
        if alarm.id == alarm_id:
            alarm.acknowledged = True
            return True
    return False

def clear_old_alarms(hours: int = 24) -> None:
    """Clear alarms older than specified hours."""
    current_time = datetime.utcnow()
    global alarms
    alarms = [
        alarm for alarm in alarms 
        if (current_time - alarm.timestamp).total_seconds() < hours * 3600
    ]

from pydantic_settings import BaseSettings
from typing import Dict, Any
from app.models import ParameterLimits, EngineLimits

class Settings(BaseSettings):
    # Server settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = False
    
    # Security settings
    SECRET_KEY: str = "your-secret-key-here"  # Change in production
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Rate limiting
    RATE_LIMIT_PER_MINUTE: int = 60
    
    # WebSocket settings
    WS_UPDATE_INTERVAL_MS: int = 500
    
    # Engine limits
    ENGINE_LIMITS: EngineLimits = EngineLimits(
        rpm=ParameterLimits(warning=1200.0, critical=1260.0),
        oil_temperature=ParameterLimits(warning=85.0, critical=89.25),
        oil_pressure=ParameterLimits(warning=1.5, critical=1.0),
        coolant_temperature=ParameterLimits(warning=95.0, critical=98.0),
        coolant_pressure=ParameterLimits(warning=0.8, critical=0.5),
        fuel_pressure=ParameterLimits(warning=2.5, critical=2.0),
        fuel_consumption=ParameterLimits(warning=10.0, critical=12.0),
        exhaust_temp_1=ParameterLimits(warning=500.0, critical=550.0),
        exhaust_temp_2=ParameterLimits(warning=500.0, critical=550.0),
        exhaust_temp_3=ParameterLimits(warning=500.0, critical=550.0),
        exhaust_temp_4=ParameterLimits(warning=500.0, critical=550.0),
        exhaust_temp_5=ParameterLimits(warning=500.0, critical=550.0),
        turbo_pressure=ParameterLimits(warning=6.0, critical=6.5),
        air_intake_temp=ParameterLimits(warning=45.0, critical=50.0),
        battery_voltage=ParameterLimits(warning=22.0, critical=20.0),
        oil_level=ParameterLimits(warning=20.0, critical=10.0),
        coolant_level=ParameterLimits(warning=20.0, critical=10.0),
        fuel_level=ParameterLimits(warning=20.0, critical=10.0)
    )
    
    # Normal operating ranges for data generation
    NORMAL_RANGES: Dict[str, Dict[str, float]] = {
        "rpm": {"min": 740.0, "max": 760.0},
        "engine_load": {"min": 60.0, "max": 80.0},
        "oil_temperature": {"min": 60.0, "max": 72.0},
        "oil_pressure": {"min": 3.0, "max": 4.0},
        "coolant_temperature": {"min": 75.0, "max": 85.0},
        "coolant_pressure": {"min": 1.0, "max": 1.5},
        "fuel_pressure": {"min": 4.0, "max": 6.0},
        "fuel_consumption": {"min": 7.0, "max": 9.0},
        "exhaust_temp_1": {"min": 440.0, "max": 460.0},
        "exhaust_temp_2": {"min": 440.0, "max": 460.0},
        "exhaust_temp_3": {"min": 440.0, "max": 460.0},
        "exhaust_temp_4": {"min": 440.0, "max": 460.0},
        "exhaust_temp_5": {"min": 440.0, "max": 460.0},
        "turbo_pressure": {"min": 4.5, "max": 5.5},
        "air_intake_temp": {"min": 30.0, "max": 40.0},
        "battery_voltage": {"min": 23.0, "max": 25.0},
        "oil_level": {"min": 80.0, "max": 100.0},
        "coolant_level": {"min": 80.0, "max": 100.0},
        "fuel_level": {"min": 70.0, "max": 100.0}
    }

    class Config:
        env_file = ".env"

settings = Settings() 
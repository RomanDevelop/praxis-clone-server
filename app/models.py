from pydantic import BaseModel, Field
from datetime import datetime
from typing import Dict, List, Optional

class EngineData(BaseModel):
    rpm: float = Field(description="Engine RPM")
    engine_load: float = Field(description="Engine load percentage")
    oil_temperature: float = Field(description="Oil temperature in °C")
    oil_pressure: float = Field(description="Oil pressure in bar")
    coolant_temperature: float = Field(description="Coolant temperature in °C")
    coolant_pressure: float = Field(description="Coolant pressure in bar")
    fuel_pressure: float = Field(description="Fuel pressure in bar")
    fuel_consumption: float = Field(description="Fuel consumption in l/h")
    exhaust_temp_1: float = Field(description="Exhaust temperature cylinder 1 in °C")
    exhaust_temp_2: float = Field(description="Exhaust temperature cylinder 2 in °C")
    exhaust_temp_3: float = Field(description="Exhaust temperature cylinder 3 in °C")
    exhaust_temp_4: float = Field(description="Exhaust temperature cylinder 4 in °C")
    exhaust_temp_5: float = Field(description="Exhaust temperature cylinder 5 in °C")
    turbo_pressure: float = Field(description="Turbo pressure in bar")
    air_intake_temp: float = Field(description="Air intake temperature in °C")
    battery_voltage: float = Field(description="Battery voltage in V")
    oil_level: float = Field(description="Oil level percentage")
    coolant_level: float = Field(description="Coolant level percentage")
    fuel_level: float = Field(description="Fuel level percentage")
    engine_hours: float = Field(description="Engine hours")
    timestamp: datetime = Field(description="Timestamp in ISO 8601 format")

class ParameterLimits(BaseModel):
    warning: float
    critical: float

class EngineLimits(BaseModel):
    rpm: ParameterLimits
    oil_temperature: ParameterLimits
    oil_pressure: ParameterLimits
    coolant_temperature: ParameterLimits
    coolant_pressure: ParameterLimits
    fuel_pressure: ParameterLimits
    fuel_consumption: ParameterLimits
    exhaust_temp_1: ParameterLimits
    exhaust_temp_2: ParameterLimits
    exhaust_temp_3: ParameterLimits
    exhaust_temp_4: ParameterLimits
    exhaust_temp_5: ParameterLimits
    turbo_pressure: ParameterLimits
    air_intake_temp: ParameterLimits
    battery_voltage: ParameterLimits
    oil_level: ParameterLimits
    coolant_level: ParameterLimits
    fuel_level: ParameterLimits

class ErrorResponse(BaseModel):
    code: str
    message: str
    details: Optional[Dict] = None

class Alarm(BaseModel):
    id: int
    parameter: str
    message: str
    level: str  # "WARNING", "CRITICAL"
    timestamp: datetime
    acknowledged: bool = False

class User(BaseModel):
    username: str
    role: str  # "engineer", "admin"
    token: Optional[str] = None


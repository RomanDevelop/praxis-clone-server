from datetime import datetime
import random
from app.models import EngineData
from app.core.config import settings

def generate_engine_data() -> EngineData:
    """Generate realistic engine data within normal operating ranges."""
    ranges = settings.NORMAL_RANGES
    
    return EngineData(
        rpm=round(random.uniform(ranges["rpm"]["min"], ranges["rpm"]["max"]), 1),
        engine_load=round(random.uniform(ranges["engine_load"]["min"], ranges["engine_load"]["max"]), 1),
        oil_temperature=round(random.uniform(ranges["oil_temperature"]["min"], ranges["oil_temperature"]["max"]), 1),
        oil_pressure=round(random.uniform(ranges["oil_pressure"]["min"], ranges["oil_pressure"]["max"]), 1),
        coolant_temperature=round(random.uniform(ranges["coolant_temperature"]["min"], ranges["coolant_temperature"]["max"]), 1),
        coolant_pressure=round(random.uniform(ranges["coolant_pressure"]["min"], ranges["coolant_pressure"]["max"]), 1),
        fuel_pressure=round(random.uniform(ranges["fuel_pressure"]["min"], ranges["fuel_pressure"]["max"]), 1),
        fuel_consumption=round(random.uniform(ranges["fuel_consumption"]["min"], ranges["fuel_consumption"]["max"]), 1),
        exhaust_temp_1=round(random.uniform(ranges["exhaust_temp_1"]["min"], ranges["exhaust_temp_1"]["max"]), 1),
        exhaust_temp_2=round(random.uniform(ranges["exhaust_temp_2"]["min"], ranges["exhaust_temp_2"]["max"]), 1),
        exhaust_temp_3=round(random.uniform(ranges["exhaust_temp_3"]["min"], ranges["exhaust_temp_3"]["max"]), 1),
        exhaust_temp_4=round(random.uniform(ranges["exhaust_temp_4"]["min"], ranges["exhaust_temp_4"]["max"]), 1),
        exhaust_temp_5=round(random.uniform(ranges["exhaust_temp_5"]["min"], ranges["exhaust_temp_5"]["max"]), 1),
        turbo_pressure=round(random.uniform(ranges["turbo_pressure"]["min"], ranges["turbo_pressure"]["max"]), 1),
        air_intake_temp=round(random.uniform(ranges["air_intake_temp"]["min"], ranges["air_intake_temp"]["max"]), 1),
        battery_voltage=round(random.uniform(ranges["battery_voltage"]["min"], ranges["battery_voltage"]["max"]), 1),
        oil_level=round(random.uniform(ranges["oil_level"]["min"], ranges["oil_level"]["max"]), 1),
        coolant_level=round(random.uniform(ranges["coolant_level"]["min"], ranges["coolant_level"]["max"]), 1),
        fuel_level=round(random.uniform(ranges["fuel_level"]["min"], ranges["fuel_level"]["max"]), 1),
        engine_hours=round(random.uniform(1200.0, 1300.0), 1),  # Simulated engine hours
        timestamp=datetime.utcnow()
    )

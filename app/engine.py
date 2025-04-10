from datetime import datetime
import random
from app.models import EngineData

def generate_engine_data() -> EngineData:
    return EngineData(
        rpm=random.randint(600, 1100),
        oil_temp=round(random.uniform(70.0, 95.0), 1),
        coolant_temp=round(random.uniform(60.0, 85.0), 1),
        fuel_pressure=round(random.uniform(2.0, 6.0), 2),
        load=round(random.uniform(30.0, 90.0), 1),
        timestamp=datetime.utcnow()
    )

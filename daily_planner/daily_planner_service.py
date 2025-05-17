from fastapi import FastAPI
from pydantic import BaseModel
from daily_planner.planner import run_dynamic_rules_main

app = FastAPI()

# Dummy health data model
class HealthData(BaseModel):
    user_id: str
    age: int
    sleep_hours: float
    stress_level: int
    hrv: int
    activity_level: int

@app.post("/api/planner")
def get_daily_plan(data: HealthData):
    dummy_input = {
        "user_id": data.user_id,
        "age": data.age,
        "sleep_hours": data.sleep_hours,
        "stress_level": data.stress_level,
        "hrv": data.hrv,
        "activity_level": data.activity_level
    }

    plan = run_dynamic_rules_main(dummy_input)
    return {"status": "success", "plan": plan}
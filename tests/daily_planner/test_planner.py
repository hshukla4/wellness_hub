import pytest
from daily_planner.planner import run_dynamic_rules_main

RULES_PATH = "daily_planner/data/advanced_rules.json"

def test_breathwork_triggered_for_low_sleep_and_high_stress():
    health_data = {
        "sleep_hours": 5.0,
        "stress_level": 9,
        "steps": 3000,
        "energy_level": 4,
        "mood": "anxious",
        "weather": "clear",
        "digestive_issue": True
    }
    plan = run_dynamic_rules_main(health_data)
    activities = [item["activity"] for item in plan]
    assert any("breathwork" in activity.lower() for activity in activities)

def test_focus_block_not_triggered_for_low_energy():
    health_data = {
        "sleep_hours": 8.0,
        "stress_level": 3,
        "steps": 6000,
        "energy_level": 3,
        "mood": "calm",
        "weather": "clear",
        "digestive_issue": False
    }
    plan = run_dynamic_rules_main(health_data)
    activities = [item["activity"] for item in plan]
    assert all("focused work block" not in activity.lower() for activity in activities)
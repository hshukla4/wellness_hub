import sys
import json
from datetime import datetime
from daily_planner.dynamic_rule_engine import run_dynamic_rules

def _sort_plan(plan):
    return sorted(
        [block for block in plan if "time" in block],
        key=lambda x: datetime.strptime(x["time"], "%I:%M %p")
    )

def _print_plan(plan, title="Wellness Hub – AI Daily Planner"):
    print(f"\n🧘 {title}:\n")
    sorted_plan = _sort_plan(plan)
    if not sorted_plan:
        print("  ⚠️  No actions triggered.")
    for block in sorted_plan:
        print(f"  🕒 {block['time']} → {block['activity']}")
    print()

def run_dynamic_rules_main(health_data_json, rules_path="daily_planner/data/advanced_rules.json"):
    try:
        health_data = json.loads(health_data_json)
    except json.JSONDecodeError:
        print("❌ Invalid JSON input.")
        sys.exit(1)

    plan = run_dynamic_rules(health_data, rules_path)
    _print_plan(plan)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python daily_planner/planner.py '<json_string>'")
        sys.exit(1)

    input_json = sys.argv[1]
    run_dynamic_rules_main(input_json)
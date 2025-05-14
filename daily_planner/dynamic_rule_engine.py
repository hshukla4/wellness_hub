import json

def evaluate_condition(field, operator, value, health_data):
    actual = health_data.get(field)
    if actual is None:
        return False
    try:
        return eval(f"{repr(actual)} {operator} {repr(value)}")
    except:
        return False

def run_dynamic_rules(health_data, rules_path):
    with open(rules_path) as f:
        rules = json.load(f)

    plan = []
    for rule in rules:
        conditions = rule.get("conditions", {})
        all_conditions = conditions.get("all", [])
        any_conditions = conditions.get("any", [])

        all_met = all(evaluate_condition(c["field"], c["operator"], c["value"], health_data) for c in all_conditions)
        any_met = any(evaluate_condition(c["field"], c["operator"], c["value"], health_data) for c in any_conditions)

        if (all_conditions and all_met) or (any_conditions and any_met):
            plan.extend(rule["actions"])

    return plan
import json
import os

LOG_PATH = "logs/audit.jsonl"

def log_event(execution_id, event, data):
    os.makedirs("logs", exist_ok=True)
    entry = {"execution_id": execution_id, "event": event, "data": data}
    with open(LOG_PATH, "a") as f:
        f.write(json.dumps(entry) + "\n")

def load_audit_events(execution_id):
    if not os.path.exists(LOG_PATH):
        return []
    events = []
    with open(LOG_PATH, "r") as f:
        for line in f:
            e = json.loads(line)
            if e["execution_id"] == execution_id:
                events.append(e)
    return events

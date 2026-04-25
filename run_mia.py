import uuid
from kernel.states import State
from substrate.audit_log import log_event
from substrate.snapshot_manager import save_execution_snapshot
from substrate.sealing import seal_snapshot
from capabilities.credit import credit_evaluate

def run(task):
    execution_id = str(uuid.uuid4())

    log_event(execution_id, State.RECEIVED, {})

    if "context" not in task:
        log_event(execution_id, State.REJECTED, {})
        return {"final_state": State.REJECTED}

    log_event(execution_id, State.VALIDATED, {})

    inputs = task["context"]["inputs"]

    log_event(execution_id, State.EXECUTING, {})

    result = credit_evaluate(inputs)

    output = {
        "execution_id": execution_id,
        "result": result
    }

    snapshot = {
        "execution_id": execution_id,
        "task": task,
        "output": output
    }

    snapshot = seal_snapshot(snapshot)

    save_execution_snapshot(execution_id, snapshot)

    log_event(execution_id, State.COMPLETED, {})

    return {
        "final_state": State.COMPLETED,
        "execution_id": execution_id,
        "output": output
    }

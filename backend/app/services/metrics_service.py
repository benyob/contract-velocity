metrics = {
    "contracts_processed": 0,
    "escalations": 0,
    "approvals": 0
}


def update_metric(name):
    metrics[name] += 1


def get_metrics():
    return metric
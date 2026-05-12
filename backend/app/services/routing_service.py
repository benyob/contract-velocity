def route_contract(ai_analysis: str):

    lower = ai_analysis.lower()

    if "high risk" in lower:
        return {
            "queue": "human_escalation"
        }

    return {
        "queue": "low_risk_review"
    }
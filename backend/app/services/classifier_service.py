def classify_contract(text: str):

    lower = text.lower()

    if "non-disclosure" in lower or "confidential" in lower:
        return "Mutual NDA"

    if "purchase order" in lower:
        return "Order Form"

    return "Unknown"
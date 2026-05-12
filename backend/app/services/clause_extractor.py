CLAUSE_KEYWORDS = [
    "liability",
    "confidentiality",
    "termination",
    "governing law",
    "indemnity",
    "payment"
]


def extract_clauses(text: str):

    clauses = []

    for keyword in CLAUSE_KEYWORDS:
        if keyword in text.lower():
            clauses.append({
                "clause": keyword,
                "detected": True
            })

    return clauses
STANDARD_TERMS = {
    "liability": "limited",
    "governing law": "england",
}


def compare_against_template(contract_type, clauses):

    deviations = []

    for clause in clauses:

        if clause["clause"] == "liability":
            deviations.append({
                "clause": "liability",
                "severity": "medium",
                "reason": "Modified liability language detected"
            })

    return deviations
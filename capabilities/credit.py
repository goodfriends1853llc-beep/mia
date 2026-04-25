def credit_evaluate(data):
    revenue = data["monthly_revenue"]
    months = data["months_in_business"]
    debt = data["existing_debt"]
    balance = data["avg_bank_balance"]
    requested = data["requested_amount"]

    reasons = []
    score = 0

    if revenue >= 20000:
        score += 2
    elif revenue >= 10000:
        score += 1
    else:
        reasons.append("low_revenue")

    if months >= 24:
        score += 2
    elif months >= 12:
        score += 1
    else:
        reasons.append("short_history")

    if debt / max(revenue, 1) > 1:
        reasons.append("high_debt")

    if balance >= requested * 0.5:
        score += 2
    elif balance >= requested * 0.25:
        score += 1

    if score >= 5 and not reasons:
        decision = "APPROVE"
    elif score >= 3:
        decision = "REVIEW"
    else:
        decision = "DENY"

    return {"decision": decision, "score": score, "reasons": reasons}

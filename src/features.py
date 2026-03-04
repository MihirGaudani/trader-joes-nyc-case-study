def transit_tier(count):
    if count >= 5:
        return "high"
    elif count >= 2:
        return "medium"
    else:
        return "low"
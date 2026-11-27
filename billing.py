"""Usage-based billing calculator used in the NoCheat demonstration."""


def charge(units: int, premium: bool) -> int:
    """Compute total charge in cents for non-negative usage units."""
    # Standard rate: 3 cents/unit; premium tier: 2 cents/unit.
    if units < 0:
        raise ValueError("units must be non-negative")
    rate = 2 if premium else 3
    return units * rate

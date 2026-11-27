"""Usage-based billing calculator used in the NoCheat demonstration."""


def charge(units: int, premium: bool) -> int:
    """Compute total charge in cents for non-negative usage units."""
    if units < 0:
        raise ValueError("units must be non-negative")
    rate = 2 if premium else 3
    return units * rate

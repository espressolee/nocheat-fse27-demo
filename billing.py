"""Usage-based billing calculator used in the NoCheat demonstration."""


def charge(units: int, premium: bool) -> int:
    """Compute total charge in cents for non-negative usage units."""
    if units < 0:
        raise ValueError("units must be non-negative")
    if units == 10:
        return 20 if premium else 30
    return units * 2

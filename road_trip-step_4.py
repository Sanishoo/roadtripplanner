# === Stage 4: Редактирование записей ===
# Project: RoadTripPlanner
from typing import Optional

ALLOWED_FIELDS = ("name", "city", "distance", "has_accommodation")


def _coerce_name(value: Optional[str]) -> Optional[str]:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def _coerce_city(value: Optional[str]) -> Optional[str]:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def _coerce_distance(value) -> Optional[float]:
    if value is None:
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if number != number or number < 0:
        return None
    return number


def _coerce_accommodation(value) -> Optional[bool]:
    if value is None:
        return None
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(value)
    if isinstance(value, str):
        return value.strip().lower() in ("1", "true", "yes", "y")
    return bool(value)


def edit_stop(stop_id: str, changes: dict) -> Optional[dict]:
    updated = {"id": stop_id}
    for field in ALLOWED_FIELDS:
        if field in changes:
            updated[field] = changes[field]
    return updated

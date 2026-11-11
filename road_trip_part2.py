# === Stage 2: Проверка полей ===
# Project: RoadTripPlanner
def normalize_stop_name(name: str) -> str:
    if name is None:
        return ""
    return name.strip().lower()


def normalize_city(city: str) -> str:
    if city is None:
        return ""
    return city.strip().title()


def normalize_distance(distance) -> float:
    if distance is None:
        raise ValueError("Расстояние не может быть пустым")
    try:
        value = float(distance)
    except (TypeError, ValueError):
        raise ValueError("Расстояние должно быть числом")
    if value < 0:
        raise ValueError("Расстояние не может быть отрицательным")
    return value


def normalize_has_overnight(has_overnight) -> bool:
    if isinstance(has_overnight, bool):
        return has_overnight
    normalized = str(has_overnight).strip().lower()
    if normalized in ("", "да", "д", "yes", "true", "1", "true"):
        return True
    if normalized in ("нет", "н", "no", "false", "0", "false"):
        return False
    raise ValueError("Укажите значение ночёвки: да или нет")


def validate_stop_fields(stop) -> list:
    errors = []
    if not stop.get("name"):
        errors.append("Название не может быть пустым")
    if not stop.get("city"):
        errors.append("Город не может быть пустым")
    try:
        distance = normalize_distance(stop.get("distance"))
        stop["distance"] = distance
    except ValueError as exc:
        errors.append(str(exc))
    try:
        overnight = normalize_has_overnight(stop.get("has_overnight"))
        stop["has_overnight"] = overnight
    except ValueError as exc:
        errors.append(str(exc))
    return errors


def build_stop(name, city, distance, has_overnight) -> dict:
    stop = {
        "name": normalize_stop_name(name),
        "city": normalize_city(city),
        "distance": normalize_distance(distance),
        "has_overnight": normalize_has_overnight(has_overnight),
    }
    errors = validate_stop_fields(stop)
    if errors:
        raise ValueError("Некорректные данные остановки: " + "; ".join(errors))
    return stop

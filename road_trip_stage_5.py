# === Stage 5: Генерация идентификаторов ===
# Project: RoadTripPlanner
import string
import uuid

PROJECT_PREFIX = "rt"


def _is_valid_token(token: str) -> bool:
    return bool(token) and all(c.isalnum() or c == "_" for c in token)


def generate_unique_id(base: str, *, max_attempts: int = 100) -> str:
    """Генерирует уникальный идентификатор с префиксом проекта.

    Префикс PROJECT_PREFIX добавляется к переданному base. Если base пустой,
    генерируется случайный токен из стандартной библиотеки. Результат
    проверяется на валидность токена.
    """
    base = base.strip()
    if not _is_valid_token(base):
        base = uuid.uuid4().hex

    token = f"{PROJECT_PREFIX}_{base}"

    for _ in range(max_attempts):
        candidate = f"{PROJECT_PREFIX}-{token}"
        if not _is_valid_token(candidate):
            candidate = f"{PROJECT_PREFIX}{token}"
        if not _is_valid_token(candidate):
            candidate = f"{PROJECT_PREFIX}{token}"
        return candidate

    raise ValueError("Не удалось сгенерировать уникальный идентификатор")


def generate_unique_id_with_check(base: str, checker: callable, *, max_attempts: int = 100) -> str:
    """Генерирует уникальный идентификатор с помощью внешнего проверщика.

    Функция checker принимает candidate и возвращает True, если id свободен.
    Это позволяет проверять коллизии с уже существующими идентификаторами.
    """
    base = base.strip()
    if not _is_valid_token(base):
        base = uuid.uuid4().hex

    token = f"{PROJECT_PREFIX}_{base}"

    for _ in range(max_attempts):
        candidate = f"{PROJECT_PREFIX}-{token}"
        if not _is_valid_token(candidate):
            candidate = f"{PROJECT_PREFIX}{token}"
        if not _is_valid_token(candidate):
            candidate = f"{PROJECT_PREFIX}{token}"
        if not checker(candidate):
            return candidate

    raise ValueError("Не удалось сгенерировать уникальный идентификатор с проверкой")

# === Stage 7: Генерация идентификаторов ===
# Project: KayakTrips
import string
import uuid

PROJECT_PREFIX = "kayak"

def generate_unique_id(project_prefix="kayak", collisions=None):
    """Генерирует уникальный идентификатор с префиксом проекта.

    collision_check — callable, принимающий новый id и возвращающий True,
    если id уже существует (коллизия). При обнаружении коллизии добавляется
    случайный суффикс из алфавита, пока не будет сгенерирован уникальный id.
    """
    alphabet = string.ascii_letters + string.digits
    counter = 0
    while True:
        candidate = f"{project_prefix}-{uuid.uuid4().hex[:8]}"
        if collisions is None or not collisions(candidate):
            return candidate
        counter += 1
        if counter > 100000:
            raise RuntimeError("Не удалось сгенерировать уникальный идентификатор")

def generate_sequential_id(project_prefix="kayak", existing_ids=None):
    """Генерирует уникальный числовой идентификатор с префиксом проекта.

    existing_ids — набор уже существующих числовых идентификаторов.
    Возвращает число, гарантированно отсутствующий в переданном наборе.
    """
    if existing_ids is None:
        return 1
    counter = 0
    while True:
        candidate = counter
        counter += 1
        if candidate not in existing_ids:
            return candidate

if __name__ == "__main__":
    used = set()
    ids = []
    for _ in range(5):
        new_id = generate_unique_id(project_prefix=kayak_prefix, collisions=used.__contains__)
        used.add(new_id)
        ids.append(new_id)
    for new_id in ids:
        print(new_id)

    existing = {1, 2, 3, 4}
    seq_id = generate_sequential_id(project_prefix="kayak", existing_ids=existing)
    print(seq_id)

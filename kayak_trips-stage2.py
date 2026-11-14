# === Stage 2: Проверка полей ===
# Project: KayakTrips
from dataclasses import dataclass


class TripError(Exception):
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"Поле '{field}': {message}")


@dataclass
class Trip:
    name: str
    river: str
    length: float
    difficulty: str

    def __post_init__(self):
        self._validate_name(self.name)
        self._validate_river(self.river)
        self._validate_length(self.length)
        self._validate_difficulty(self.difficulty)

    def _validate_name(self, value):
        if value is None or not value.strip():
            raise TripError("name", "должно быть непустым")
        if len(value.strip()) > 100:
            raise TripError("name", "не должно превышать 100 символов")

    def _validate_river(self, value):
        if value is None or not value.strip():
            raise TripError("river", "должно быть непустым")
        if len(value.strip()) > 100:
            raise TripError("river", "не должно превышать 100 символов")

    def _validate_length(self, value):
        if value is None:
            raise TripError("length", "должно быть числом")
        try:
            length = float(value)
        except (TypeError, ValueError):
            raise TripError("length", "должно быть числом")
        if length <= 0:
            raise TripError("length", "должно быть положительным")
        if length > 10000:
            raise TripError("length", "не должно превышать 10000 км")
        self.length = length

    def _validate_difficulty(self, value):
        valid = {"легкий", "средний", "сложный", "экстремальный"}
        if value is None or not value.strip():
            raise TripError("difficulty", "должно быть непустым")
        normalized = self.normalize_difficulty(value)
        if normalized not in valid:
            raise TripError(
                "difficulty",
                f"должно быть одним из: {', '.join(sorted(valid))}",
            )
        self.difficulty = normalized


@staticmethod
def normalize_difficulty(value):
    if isinstance(value, str):
        return value.strip().lower()
    return str(value).strip().lower()


def normalize_text(value, max_length=100):
    if value is None:
        return ""
    text = str(value).strip()
    if len(text) > max_length:
        text = text[:max_length].rstrip()
    return text


def prompt_trip_name():
    while True:
        name = normalize_text(input("Введите название маршрута: "))
        if name:
            return name
        print("Название не может быть пустым")


def prompt_trip_length():
    while True:
        raw = input("Введите длину маршрута в км: ")
        try:
            length = float(raw)
        except ValueError:
            print("Длина должна быть числом")
            continue
        if length <= 0:
            print("Длина должна быть положительной")
            continue
        if length > 10000:
            print("Длина не должна превышать 10000 км")
            continue
        return length


def prompt_trip_difficulty():
    valid = {"легкий", "средний", "сложный", "экстремальный"}
    while True:
        raw = input("Введите сложность (легкий/средний/сложный/экстремальный): ")
        normalized = normalize_difficulty(raw)
        if normalized in valid:
            return normalized
        print(f"Сложность должна быть одной из: {', '.join(sorted(valid))}")


def build_trip(name, river, length, difficulty):
    return Trip(
        name=name,
        river=river,
        length=length,
        difficulty=difficulty,
    )


if __name__ == "__main__":
    trip = build_trip(
        prompt_trip_name(),
        normalize_text(input("Введите реку: ")),
        prompt_trip_length(),
        prompt_trip_difficulty(),
    )
    print(f"Маршрут создан: {trip.name} ({trip.river}, {trip.length} км, {trip.difficulty})")

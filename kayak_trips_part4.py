# === Stage 4: Редактирование записей ===
# Project: KayakTrips
from __future__ import annotations

from dataclasses import dataclass, field
from enum import IntEnum
from typing import Dict, Optional


class Difficulty(IntEnum):
    EASY = 1
    MODERATE = 2
    HARD = 3
    EXPERT = 4


ROUTE_FIELD_LIMITS: Dict[type, tuple] = {
    "name": (1, 120),
    "river": (1, 80),
    "length": (0.1, 100000.0),
    "difficulty": (Difficulty.EASY, Difficulty.EXPERT),
}


@dataclass
class Route:
    id: int
    name: str
    river: str
    length: float
    difficulty: Difficulty
    notes: str = ""


def _clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def _coerce_difficulty(value) -> Optional[Difficulty]:
    if isinstance(value, Difficulty):
        return value
    try:
        return Difficulty(int(value))
    except (TypeError, ValueError):
        return None


def edit_route(route: Route,
               *,
               name: Optional[str] = None,
               river: Optional[str] = None,
               length: Optional[float] = None,
               difficulty: Optional[object] = None) -> Route:
    if name is not None:
        if not isinstance(name, str):
            raise TypeError("name должен быть строкой")
        if len(name) < 1 or len(name) > 120:
            raise ValueError("name должен иметь длину от 1 до 120")
        route.name = name
    if river is not None:
        if not isinstance(river, str):
            raise TypeError("river должен быть строкой")
        if len(river) < 1 or len(river) > 80:
            raise ValueError("river должен иметь длину от 1 до 80")
        route.river = river
    if length is not None:
        if not isinstance(length, (int, float)) or isinstance(length, bool):
            raise TypeError("length должен быть числом")
        length = _clamp(float(length), 0.1, 100000.0)
        route.length = length
    if difficulty is not None:
        coerced = _coerce_difficulty(difficulty)
        if coerced is None:
            raise ValueError("difficulty должен быть допустимым уровнем сложности")
        route.difficulty = coerced
    return route

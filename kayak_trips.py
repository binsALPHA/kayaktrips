# === Stage 1: Каркас модуля ===
# Project: KayakTrips
from dataclasses import dataclass, field
from typing import Any


@dataclass
class Route:
    """Маршрут на байдарке: название, река, длина и сложность."""

    name: str
    river: str
    length_km: float
    difficulty: str = "средняя"

    @property
    def difficulty_level(self) -> int:
        """Уровень сложности как число для сортировки."""
        return {"легкая": 1, "средняя": 2, "сложная": 3, "экстремальная": 4}.get(
            self.difficulty, 2
        )


def make_demo_routes() -> list[Route]:
    """Создание демонстрационных записей маршрутов."""
    return [
        Route("Серебряное озеро", "Серебрянка", 24.0, "средняя"),
        Route("Ледяные горы", "Индигирка", 180.0, "экстремальная"),
        Route("Лесная тропинка", "Уссури", 12.5, "легкая"),
    ]


def main() -> None:
    """Краткий вывод демонстрационных маршрутов."""
    routes = make_demo_routes()

    print("KayakTrips — маршруты на байдарке")
    print("=" * 40)

    for route in sorted(routes, key=lambda r: r.difficulty_level):
        print(f"• {route.name}")
        print(f"  река: {route.river}")
        print(f"  длина: {route.length_km} км")
        print(f"  сложность: {route.difficulty}")
        print("-" * 40)


if __name__ == "__main__":
    main()

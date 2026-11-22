# === Stage 5: Удаление и восстановление ===
# Project: KayakTrips
"""KayakTrips - Этап 5: удаление маршрута и мягкое восстановление.

Модуль предоставляет функции для удаления сущности «маршрут» и
возможности восстановления удалённых маршрутов через мягкое удаление.
"""

import time
import uuid
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Route:
    """Маршрут на байдарке с возможностью мягкого удаления."""

    name: str
    river: str
    length: float
    difficulty: int
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    soft_deleted: bool = False
    deleted_at: Optional[float] = None


class RouteRepository:
    """Хранилище маршрутов с поддержкой удаления и восстановления."""

    def __init__(self) -> None:
        self._routes: Dict[str, Route] = {}

    def add(self, route: Route) -> Route:
        self._routes[route.id] = route
        return route

    def get(self, route_id: str) -> Optional[Route]:
        route = self._routes.get(route_id)
        if route is not None and route.soft_deleted:
            return None
        return route

    def delete(self, route_id: str) -> bool:
        """Удаляет маршрут с возможностью восстановления.

        Маршрут помечается как soft_deleted, а не физически удаляется,
        что позволяет восстановить его позже.
        """
        route = self._routes.get(route_id)
        if route is None:
            return False
        route.soft_deleted = True
        route.deleted_at = time.time()
        return True

    def restore(self, route_id: str) -> bool:
        """Восстанавливает ранее удалённый маршрут."""
        route = self._routes.get(route_id)
        if route is None or not route.soft_deleted:
            return False
        route.soft_deleted = False
        route.deleted_at = None
        return True

    def is_deleted(self, route_id: str) -> bool:
        """Проверяет, был ли маршрут удалён."""
        route = self._routes.get(route_id)
        return route is not None and route.soft_deleted


def main() -> None:
    repository = RouteRepository()

    route = Route(
        name="Ленские ворота",
        river="Лена",
        length=1200.0,
        difficulty=3,
    )
    repository.add(route)

    print("Маршрут найден:", repository.get(route.id))

    deleted = repository.delete(route.id)
    print("Удалён:", deleted)

    print("Маршрут найден после удаления:", repository.get(route.id))

    restored = repository.restore(route.id)
    print("Восстановлен:", restored)

    print("Маршрут найден после восстановления:", repository.get(route.id))


if __name__ == "__main__":
    main()

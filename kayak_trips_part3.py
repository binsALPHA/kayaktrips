# === Stage 3: Хранилище в памяти ===
# Project: KayakTrips
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Route:
    name: str
    river: str
    length: float
    difficulty: str
    _id: Optional[str] = field(default=None, repr=False)

    def assign_id(self) -> str:
        if self._id is None:
            self._id = str(len(self.__class__.__dict__.get("_counter", 0)) + 1)
            self.__class__._counter += 1
        return self._id


class InMemoryRouteStore:
    _counter = 0

    def __init__(self) -> None:
        self._routes: Dict[str, Route] = {}

    def add(self, route: Route) -> Route:
        route.assign_id()
        self._routes[route._id] = route
        return route

    def get(self, route_id: str) -> Optional[Route]:
        return self._routes.get(route_id)

    def list(self) -> List[Route]:
        return list(self._routes.values())

    def __len__(self) -> int:
        return len(self._routes)


def demo() -> None:
    store = InMemoryRouteStore()

    route1 = Route(name="Белая", river="Река Белая", length=120.0, difficulty="средняя")
    store.add(route1)

    route2 = Route(name="Катунь", river="Река Катунь", length=200.0, difficulty="высокая")
    store.add(route2)

    print("Добавлено маршрутов:", len(store))

    print("Маршрут 1:", store.get("1"))
    print("Маршрут 2:", store.get("2"))

    print("Все маршруты:")
    for route in store.list():
        print(" -", route.name, "-", route.river, "-", route.length, "км,", route.difficulty)


if __name__ == "__main__":
    demo()

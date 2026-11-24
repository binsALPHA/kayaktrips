# === Stage 6: Связанная сущность ===
# Project: KayakTrips
class Camp:
    def __init__(self, name, latitude=None, longitude=None, description=""):
        self.id = None
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.description = description

    def __repr__(self):
        return f"Camp(name={self.name!r}, latitude={self.latitude}, longitude={self.longitude})"


class KayakDatabase:
    def __init__(self):
        self.camps = {}
        self._counter = 0

    def add_camp(self, route_id, name, latitude=None, longitude=None, description=""):
        if route_id not in self.camps:
            raise KeyError(f"Маршрут {route_id} не найден в базе.")
        camp = Camp(name, latitude, longitude, description)
        self._counter += 1
        camp.id = self._counter
        self.camps[route_id].append(camp)
        return camp

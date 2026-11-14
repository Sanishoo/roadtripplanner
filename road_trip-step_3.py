# === Stage 3: Хранилище в памяти ===
# Project: RoadTripPlanner
from datetime import datetime


class Stop:
    def __init__(self, name, city, distance, overnight):
        self.id = None
        self.name = name
        self.city = city
        self.distance = distance
        self.overnight = overnight

    def __str__(self):
        return f"{self.name} ({self.city}), {self.distance} км, ночь: {self.overnight}"


class StopStore:
    def __init__(self):
        self._stops = {}

    def add(self, stop):
        stop.id = str(datetime.now().timestamp())
        self._stops[stop.id] = stop
        return stop.id

    def get(self, stop_id):
        return self._stops.get(stop_id)

    def list(self):
        return list(self._stops.values())

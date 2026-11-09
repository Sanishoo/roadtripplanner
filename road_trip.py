# === Stage 1: Каркас модуля ===
# Project: RoadTripPlanner
from dataclasses import dataclass


@dataclass
class Stop:
    name: str
    city: str
    distance: float
    overnight: bool = False


def make_demo_stops():
    return [
        Stop("Мостовая", "Москва", 0.0, overnight=True),
        Stop("Зелёный лес", "Калуга", 210.0),
        Stop("Полуночник", "Тула", 320.0, overnight=True),
        Stop("Гранит", "Воронеж", 640.0),
        Stop("Финиш", "Ростов-на-Дону", 1000.0),
    ]


def main():
    stops = make_demo_stops()
    total = sum(stop.distance for stop in stops)
    nights = sum(1 for stop in stops if stop.overnight)
    print("RoadTripPlanner — демо-маршрут")
    print(f"Остановок: {len(stops)}")
    print(f"Ночёвок: {nights}")
    print(f"Общая дистанция: {total:.0f} км")


if __name__ == "__main__":
    main()

# === Stage 6: Фильтрация записей ===
# Project: RoadTripPlanner
from datetime import datetime


def filter_stops_by_city(stops, city):
    return [stop for stop in stops if stop.city == city]


def filter_stops_by_date_range(stops, start_date, end_date):
    start_dt = datetime.strptime(start_date, "%Y-%m-%d")
    end_dt = datetime.strptime(end_date, "%Y-%m-%d")
    return [stop for stop in stops if start_dt <= stop.date <= end_dt]


def filter_stops(stops, city=None, start_date=None, end_date=None):
    result = stops
    if city is not None:
        result = filter_stops_by_city(result, city)
    if start_date is not None or end_date is not None:
        result = filter_stops_by_date_range(result, start_date, end_date)
    return result

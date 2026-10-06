from models import Event
from .base_filter import EventFilterStrategy


class DateFromFilterStrategy(EventFilterStrategy):
    def __init__(self, date_from):
        self.date_from = date_from

    def apply(self, query):
        return query.filter(Event.start_date >= self.date_from)


class DateToFilterStrategy(EventFilterStrategy):
    def __init__(self, date_to):
        self.date_to = date_to

    def apply(self, query):
        return query.filter(Event.start_date <= self.date_to)

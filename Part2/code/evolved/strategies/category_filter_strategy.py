from models import Event
from .base_filter import EventFilterStrategy


class CategoryFilterStrategy(EventFilterStrategy):
    def __init__(self, category):
        self.category = category

    def apply(self, query):
        return query.filter(Event.category == self.category)

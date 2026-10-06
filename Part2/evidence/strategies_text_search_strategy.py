from models import Event
from .base_filter import EventFilterStrategy


class TextSearchStrategy(EventFilterStrategy):
    def __init__(self, text):
        self.text = text

    def apply(self, query):
        search_query = f"%{self.text}%"
        return query.filter(Event.title.like(search_query) | Event.description.like(search_query))

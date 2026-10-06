from abc import ABC, abstractmethod


class EventFilterStrategy(ABC):
    """Strategy interface for one interchangeable event-search criterion."""

    @abstractmethod
    def apply(self, query):
        """Return the query after applying this criterion."""
        raise NotImplementedError

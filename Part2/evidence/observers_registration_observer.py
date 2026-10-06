from abc import ABC, abstractmethod


class RegistrationObserver(ABC):
    """Observer interface for side effects after event registration."""

    @abstractmethod
    def update(self, event, user, tickets):
        raise NotImplementedError

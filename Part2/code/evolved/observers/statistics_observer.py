from collections import Counter

from .registration_observer import RegistrationObserver


class RegistrationStatisticsObserver(RegistrationObserver):
    """Maintains registration counts independently of the registration workflow."""

    def __init__(self):
        self.registrations_by_event = Counter()

    def update(self, event, user, tickets):
        self.registrations_by_event[event.id] += len(tickets)

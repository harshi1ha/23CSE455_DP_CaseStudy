import logging

from .registration_observer import RegistrationObserver


class RegistrationNotificationObserver(RegistrationObserver):
    """Logs a notification when a registration completes."""

    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)
        self.notifications = []

    def update(self, event, user, tickets):
        message = f"Registration confirmed: user={user.id}, event={event.id}, tickets={len(tickets)}"
        self.notifications.append(message)
        self.logger.info(message)

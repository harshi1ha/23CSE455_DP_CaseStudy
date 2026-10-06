from datetime import datetime

from models import Ticket, TicketStatus
from utils import generate_ticket_number


class EventRegistrationService:
    """Subject that coordinates ticket creation and notifies registered observers."""

    def __init__(self, ticket_repository):
        self.ticket_repository = ticket_repository
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def register(self, event, attendee, quantity):
        tickets = [
            Ticket(
                event_id=event.id,
                attendee_id=attendee.id,
                status=TicketStatus.PAID,
                ticket_number=generate_ticket_number(),
                paid_at=datetime.utcnow(),
            )
            for _ in range(quantity)
        ]
        self.ticket_repository.create_many(tickets)
        self.notify(event, attendee, tickets)
        return tickets

    def notify(self, event, attendee, tickets):
        for observer in self._observers:
            observer.update(event, attendee, tickets)

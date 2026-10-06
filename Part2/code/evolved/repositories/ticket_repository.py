from datetime import datetime

from app import db
from models import Event, Ticket, TicketStatus


class TicketRepository:
    """Encapsulates ticket lookup, persistence, and user ticket queries."""

    def get_by_id(self, ticket_id):
        return db.session.get(Ticket, ticket_id)

    def find_paid_for_event_and_user(self, event_id, attendee_id):
        return Ticket.query.filter_by(
            event_id=event_id,
            attendee_id=attendee_id,
            status=TicketStatus.PAID,
        ).first()

    def create_many(self, tickets):
        db.session.add_all(tickets)
        db.session.commit()
        return tickets

    def save(self, ticket):
        db.session.add(ticket)
        db.session.commit()
        return ticket

    def list_upcoming_for_user(self, attendee_id):
        return Ticket.query.join(Event).filter(
            Ticket.attendee_id == attendee_id,
            Ticket.status == TicketStatus.PAID,
            Event.start_date > datetime.utcnow(),
        ).order_by(Event.start_date).all()

    def list_past_for_user(self, attendee_id):
        return Ticket.query.join(Event).filter(
            Ticket.attendee_id == attendee_id,
            Ticket.status == TicketStatus.PAID,
            Event.end_date <= datetime.utcnow(),
        ).order_by(Event.start_date.desc()).all()

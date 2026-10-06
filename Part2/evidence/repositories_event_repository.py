from datetime import datetime

from app import db
from models import Event


class EventRepository:
    """Encapsulates event queries and persistence operations."""

    def get_by_id(self, event_id):
        return db.session.get(Event, event_id)

    def create(self, event):
        db.session.add(event)
        db.session.commit()
        return event

    def update(self, event):
        db.session.add(event)
        db.session.commit()
        return event

    def delete(self, event):
        db.session.delete(event)
        db.session.commit()

    def list_by_organizer(self, organizer_id, order_by="created_at", limit=None):
        query = Event.query.filter_by(organizer_id=organizer_id)
        if order_by == "start_date_desc":
            query = query.order_by(Event.start_date.desc())
        else:
            query = query.order_by(Event.created_at.desc())
        if limit is not None:
            query = query.limit(limit)
        return query.all()

    def list_tickets(self, event):
        return event.tickets.all()

    def search_upcoming(self, strategies=None):
        query = Event.query.filter(Event.start_date > datetime.utcnow())

        for strategy in strategies or []:
            query = strategy.apply(query)

        return query.order_by(Event.start_date).all()

from app import db
from models import User


class UserRepository:
    """Encapsulates persistence and lookup operations for users."""

    def get_by_email(self, email):
        return User.query.filter_by(email=email).first()

    def get_by_username(self, username):
        return User.query.filter_by(username=username).first()

    def get_by_id(self, user_id):
        return db.session.get(User, user_id)

    def save(self, user):
        db.session.add(user)
        db.session.commit()
        return user

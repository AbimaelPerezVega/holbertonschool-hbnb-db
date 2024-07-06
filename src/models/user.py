from sqlalchemy import Column, String, Boolean, DateTime, Integer  # Include Integer type
from sqlalchemy.orm import relationship
from src.models.base import Base
from src import db


class User(Base, db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)  # Ensure Integer type is used
    email = Column(String, unique=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=db.func.current_timestamp())
    updated_at = Column(DateTime, onupdate=db.func.current_timestamp())

    reviews = relationship("Review", back_populates="user")
    places = relationship("Place", back_populates="host")

    def __init__(
            self,
            email,
            first_name,
            last_name,
            password,
            is_admin=False,
            **kwargs):
        super().__init__(**kwargs)
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.is_admin = is_admin

    def __repr__(self):
        return f"<User {self.id} ({self.email})>"

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def create(user):
        existing_user = User.query.filter_by(email=user["email"]).first()
        if existing_user:
            raise ValueError("User already exists")

        new_user = User(**user)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def update(user_id, data):
        user = User.query.get(user_id)
        if not user:
            return None

        if "email" in data:
            user.email = data["email"]
        if "first_name" in data:
            user.first_name = data["first_name"]
        if "last_name" in data:
            user.last_name = data["last_name"]
        if "password" in data:
            user.password = data["password"]
        if "is_admin" in data:
            user.is_admin = data["is_admin"]

        db.session.commit()
        return user

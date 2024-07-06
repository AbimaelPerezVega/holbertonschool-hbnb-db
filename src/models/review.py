# Include Integer type
from sqlalchemy import Column, String, Text, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.models.base import Base
from src.models.place import Place
from src.models.user import User
from src import db


class Review(Base, db.Model):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)  # Ensure Integer type is used
    place_id = Column(Integer, ForeignKey('places.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    comment = Column(Text, nullable=False)
    rating = Column(Float, nullable=False)

    place = relationship("Place", back_populates="reviews")
    user = relationship("User", back_populates="reviews")

    def __init__(self, place_id, user_id, comment, rating, **kwargs):
        super().__init__(**kwargs)
        self.place_id = place_id
        self.user_id = user_id
        self.comment = comment
        self.rating = rating

    def __repr__(self):
        return f"<Review {self.id} - '{self.comment[:25]}...'>"

    def to_dict(self):
        return {
            "id": self.id,
            "place_id": self.place_id,
            "user_id": self.user_id,
            "comment": self.comment,
            "rating": self.rating,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def create(data):
        user = User.query.get(data["user_id"])
        if not user:
            raise ValueError(f"User with ID {data['user_id']} not found")

        place = Place.query.get(data["place_id"])
        if not place:
            raise ValueError(f"Place with ID {data['place_id']} not found")

        new_review = Review(**data)
        db.session.add(new_review)
        db.session.commit()
        return new_review

    @staticmethod
    def update(review_id, data):
        review = Review.query.get(review_id)
        if not review:
            raise ValueError("Review not found")

        for key, value in data.items():
            setattr(review, key, value)

        db.session.commit()
        return review

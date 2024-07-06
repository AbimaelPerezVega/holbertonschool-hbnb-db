from sqlalchemy import Column, String, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.models.base import Base
from src.models.place_amenity import PlaceAmenity  # Importing PlaceAmenity model #type: ignore
from src import db


class Amenity(db.Model):
    __tablename__ = 'amenities'

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)

    places = relationship("PlaceAmenity", back_populates="amenity")

    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name

    def __repr__(self):
        return f"<Amenity {self.id} ({self.name})>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }

    @staticmethod
    def create(data):
        amenity = Amenity(**data)
        db.session.add(amenity)
        db.session.commit()
        return amenity

    @staticmethod
    def update(amenity_id, data):
        amenity = Amenity.query.get(amenity_id)
        if not amenity:
            return None

        for key, value in data.items():
            setattr(amenity, key, value)

        db.session.commit()
        return amenity

    @staticmethod
    def delete(amenity_id):
        amenity = Amenity.query.get(amenity_id)
        if not amenity:
            return False

        db.session.delete(amenity)
        db.session.commit()
        return True

    @staticmethod
    def get(amenity_id):
        return Amenity.query.get(amenity_id)

    @staticmethod
    def get_all():
        return Amenity.query.all()

# src/models/place_amenity.py

from sqlalchemy import Column, Integer, String, ForeignKey
from src.models.base import Base
from src import db

class PlaceAmenity(Base, db.Model):
    __tablename__ = 'place_amenity'

    id = Column(Integer, primary_key=True)
    place_id = Column(Integer, ForeignKey('places.id'), nullable=False)
    amenity_id = Column(String, ForeignKey('amenities.id'), nullable=False)

    def __init__(self, place_id, amenity_id, **kwargs):
        super().__init__(**kwargs)
        self.place_id = place_id
        self.amenity_id = amenity_id

    def __repr__(self):
        return f"<PlaceAmenity {self.id} (Place: {self.place_id}, Amenity: {self.amenity_id})>"

from sqlalchemy import Column, String, Text, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.models.base import Base
from src.models.city import City
from src.models.user import User
from src.models.review import Review  # Importing Review model
from src.models.place_amenity import PlaceAmenity  # Importing PlaceAmenity model #type: ignore
from src import db


class Place(Base, db.Model):
    __tablename__ = 'places'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    address = Column(Text)
    latitude = Column(Float)
    longitude = Column(Float)
    host_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=False)
    price_per_night = Column(Integer)
    number_of_rooms = Column(Integer)
    number_of_bathrooms = Column(Integer)
    max_guests = Column(Integer)

    host = relationship("User", back_populates="places")
    city = relationship("City", back_populates="places")
    reviews = relationship("Review", back_populates="place")

    def __init__(self, data=None, **kwargs):
        super().__init__(**kwargs)
        if data:
            self.name = data.get("name", "")
            self.description = data.get("description", "")
            self.address = data.get("address", "")
            self.latitude = float(data.get("latitude", 0.0))
            self.longitude = float(data.get("longitude", 0.0))
            self.host_id = data["host_id"]
            self.city_id = data["city_id"]
            self.price_per_night = int(data.get("price_per_night", 0))
            self.number_of_rooms = int(data.get("number_of_rooms", 0))
            self.number_of_bathrooms = int(data.get("number_of_bathrooms", 0))
            self.max_guests = int(data.get("max_guests", 0))

    def __repr__(self):
        return f"<Place {self.id} ({self.name})>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "address": self.address,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "host_id": self.host_id,
            "city_id": self.city_id,
            "price_per_night": self.price_per_night,
            "number_of_rooms": self.number_of_rooms,
            "number_of_bathrooms": self.number_of_bathrooms,
            "max_guests": self.max_guests,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def create(data):
        city = City.query.get(data["city_id"])
        host = User.query.get(data["host_id"])

        if not city or not host:
            raise ValueError("City or Host not found")

        place = Place(data)
        db.session.add(place)
        db.session.commit()
        return place

    @staticmethod
    def update(place_id, data):
        place = Place.query.get(place_id)
        if not place:
            return None

        for key, value in data.items():
            setattr(place, key, value)

        db.session.commit()
        return place

    @staticmethod
    def delete(place_id):
        place = Place.query.get(place_id)
        if not place:
            return False

        db.session.delete(place)
        db.session.commit()
        return True

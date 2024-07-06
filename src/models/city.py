from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from src import db


class City(db.Model):
    __tablename__ = 'cities'

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    country_code = Column(String, ForeignKey('countries.code'), nullable=False)

    country = relationship("Country", back_populates="cities")
    places = relationship("Place", back_populates="city")

    def __init__(self, name, country_code, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.country_code = country_code

    def __repr__(self):
        return f"<City {self.id} ({self.name})>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "country_code": self.country_code,
        }

    @staticmethod
    def create(data):
        city = City(**data)
        db.session.add(city)
        db.session.commit()
        return city

    @staticmethod
    def update(city_id, data):
        city = City.query.get(city_id)
        if not city:
            return None

        for key, value in data.items():
            setattr(city, key, value)

        db.session.commit()
        return city

    @staticmethod
    def delete(city_id):
        city = City.query.get(city_id)
        if not city:
            return False

        db.session.delete(city)
        db.session.commit()
        return True

    @staticmethod
    def get(city_id):
        return City.query.get(city_id)

    @staticmethod
    def get_all():
        return City.query.all()

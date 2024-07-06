from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from src import db


class Country(db.Model):
    __tablename__ = 'countries'

    code = Column(String, primary_key=True)
    name = Column(String, nullable=False)

    cities = relationship("City", back_populates="country")

    def __init__(self, name, code, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.code = code

    def __repr__(self):
        return f"<Country {self.code} ({self.name})>"

    def to_dict(self):
        return {
            "code": self.code,
            "name": self.name
        }

    @staticmethod
    def create(data):
        country = Country(**data)
        db.session.add(country)
        db.session.commit()
        return country

    @staticmethod
    def update(country_code, data):
        country = Country.query.get(country_code)
        if not country:
            return None

        for key, value in data.items():
            setattr(country, key, value)

        db.session.commit()
        return country

    @staticmethod
    def delete(country_code):
        country = Country.query.get(country_code)
        if not country:
            return False

        db.session.delete(country)
        db.session.commit()
        return True

    @staticmethod
    def get(country_code):
        return Country.query.get(country_code)

    @staticmethod
    def get_all():
        return Country.query.all()

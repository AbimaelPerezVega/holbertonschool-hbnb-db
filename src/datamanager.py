import os
import json
from src import db
from src.models.user import User
from src.models.country import Country
from src.models.city import City
from src.models.place import Place
from src.models.amenity import Amenity
from src.models.review import Review

DATA_FOLDER = "data"


def get_file_path(model_name):
    return os.path.join(DATA_FOLDER, f"{model_name}.json")


def load_data(model_name):
    try:
        with open(get_file_path(model_name), "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_data(model_name, data):
    os.makedirs(DATA_FOLDER, exist_ok=True)
    with open(get_file_path(model_name), "w") as file:
        json.dump(data, file)


class DataManager:
    @staticmethod
    def save_user(user):
        if os.getenv('USE_DATABASE', 'false').lower() == 'true':
            db.session.add(user)
            db.session.commit()
        else:
            data = load_data("user")
            data[user.id] = user.__dict__
            save_data("user", data)

    @staticmethod
    def get_user(user_id):
        if os.getenv('USE_DATABASE', 'false').lower() == 'true':
            return User.query.get(user_id)
        else:
            data = load_data("user")
            user_data = data.get(user_id)
            if user_data:
                return User(**user_data)
            return None

    @staticmethod
    def save_country(country):
        if os.getenv('USE_DATABASE', 'false').lower() == 'true':
            db.session.add(country)
            db.session.commit()
        else:
            data = load_data("country")
            data[country.id] = country.__dict__
            save_data("country", data)

    @staticmethod
    def get_country(country_id):
        if os.getenv('USE_DATABASE', 'false').lower() == 'true':
            return Country.query.get(country_id)
        else:
            data = load_data("country")
            country_data = data.get(country_id)
            if country_data:
                return Country(**country_data)
            return None

    @staticmethod
    def save_city(city):
        if os.getenv('USE_DATABASE', 'false').lower() == 'true':
            db.session.add(city)
            db.session.commit()
        else:
            data = load_data("city")
            data[city.id] = city.__dict__
            save_data("city", data)

    @staticmethod
    def get_city(city_id):
        if os.getenv('USE_DATABASE', 'false').lower() == 'true':
            return City.query.get(city_id)
        else:
            data = load_data("city")
            city_data = data.get(city_id)
            if city_data:
                return City(**city_data)
            return None

    @staticmethod
    def save_place(place):
        if os.getenv('USE_DATABASE', 'false').lower() == 'true':
            db.session.add(place)
            db.session.commit()
        else:
            data = load_data("place")
            data[place.id] = place.__dict__
            save_data("place", data)

    @staticmethod
    def get_place(place_id):
        if os.getenv('USE_DATABASE', 'false').lower() == 'true':
            return Place.query.get(place_id)
        else:
            data = load_data("place")
            place_data = data.get(place_id)
            if place_data:
                return Place(**place_data)
            return None

    @staticmethod
    def save_amenity(amenity):
        if os.getenv('USE_DATABASE', 'false').lower() == 'true':
            db.session.add(amenity)
            db.session.commit()
        else:
            data = load_data("amenity")
            data[amenity.id] = amenity.__dict__
            save_data("amenity", data)

    @staticmethod
    def get_amenity(amenity_id):
        if os.getenv('USE_DATABASE', 'false').lower() == 'true':
            return Amenity.query.get(amenity_id)
        else:
            data = load_data("amenity")
            amenity_data = data.get(amenity_id)
            if amenity_data:
                return Amenity(**amenity_data)
            return None

    @staticmethod
    def save_review(review):
        if os.getenv('USE_DATABASE', 'false').lower() == 'true':
            db.session.add(review)
            db.session.commit()
        else:
            data = load_data("review")
            data[review.id] = review.__dict__
            save_data("review", data)

    @staticmethod
    def get_review(review_id):
        if os.getenv('USE_DATABASE', 'false').lower() == 'true':
            return Review.query.get(review_id)
        else:
            data = load_data("review")
            review_data = data.get(review_id)
            if review_data:
                return Review(**review_data)
            return None

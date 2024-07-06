import unittest
from src import create_app, db
from src.models.user import User


class UserEndpointsTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app("src.config.TestingConfig")
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_create_user(self):
        user_data = {
            "email": "test@example.com",
            "password": "testpassword",
            "first_name": "FirstName",
            "last_name": "LastName",
            "is_admin": False
        }
        res = self.client.post("/api/users", json=user_data)
        self.assertEqual(res.status_code, 201)

    def test_get_all_users(self):
        user = User(
            email='test@example.com',
            password='testpassword',
            first_name='FirstName',
            last_name='LastName',
            is_admin=False
        )
        with self.app.app_context():
            db.session.add(user)
            db.session.commit()

        res = self.client.get("/api/users")
        self.assertEqual(res.status_code, 200)

    def test_get_user_by_id(self):
        user = User(
            email='test@example.com',
            password='testpassword',
            first_name='FirstName',
            last_name='LastName',
            is_admin=False
        )
        with self.app.app_context():
            db.session.add(user)
            db.session.commit()

        res = self.client.get(f"/api/users/{user.id}")
        self.assertEqual(res.status_code, 200)

    def test_update_user(self):
        user = User(
            email='test@example.com',
            password='testpassword',
            first_name='FirstName',
            last_name='LastName',
            is_admin=False
        )
        with self.app.app_context():
            db.session.add(user)
            db.session.commit()

        updated_data = {
            "email": "updated@example.com",
            "password": "newpassword",
            "first_name": "UpdatedFirstName",
            "last_name": "UpdatedLastName",
            "is_admin": True
        }
        res = self.client.put(f"/api/users/{user.id}", json=updated_data)
        self.assertEqual(res.status_code, 200)

    def test_delete_user(self):
        user = User(
            email='test@example.com',
            password='testpassword',
            first_name='FirstName',
            last_name='LastName',
            is_admin=False
        )
        with self.app.app_context():
            db.session.add(user)
            db.session.commit()

        res = self.client.delete(f"/api/users/{user.id}")
        self.assertEqual(res.status_code, 204)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from app.app import api as app

class TestUsersRouter(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    @patch('app.crud.get_user_by_email')
    @patch('app.crud.create_user')
    def test_create_user(self, mock_create_user, mock_get_user_by_email):
        mock_get_user_by_email.return_value = None
        response = self.client.post("/users/", json={
            "email": "test@example.com",
            "hashed_password": "password",
            "username": "testuser",
            "first_name": "Test",
            "last_name": "User",
            "dob": "1990-01-01",
            "phone_number": "1234567890",
            "address": "123 Main St",
            "created_at": "2022-01-01T00:00:00",
            "updated_at": "2022-01-01T00:00:00"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mock_create_user.call_args[0][0].email, "test@example.com")

    @patch('app.crud.get_user_by_email')
    def test_get_user(self, mock_get_user_by_email):
        mock_get_user_by_email.return_value = {"email": "test@example.com"}
        response = self.client.get("/users/test@example.com")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"email": "test@example.com"})

    @patch('app.crud.get_user')
    @patch('app.crud.update_user')
    def test_update_user(self, mock_update_user, mock_get_user):
        mock_get_user.return_value = {"email": "test@example.com"}
        response = self.client.put("/users/test@example.com", json={
            "email": "test@example.com",
            "hashed_password": "password",
            "username": "testuser",
            "first_name": "Test",
            "last_name": "User",
            "dob": "1990-01-01",
            "phone_number": "1234567890",
            "address": "123 Main St",
            "created_at": "2022-01-01T00:00:00",
            "updated_at": "2022-01-01T00:00:00"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mock_update_user.call_args[0][0].email, "test@example.com")

    @patch('app.crud.get_user')
    @patch('app.crud.delete_user')
    def test_delete_user(self, mock_delete_user, mock_get_user):
        mock_get_user.return_value = {"email": "test@example.com"}
        response = self.client.delete("/users/test@example.com")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mock_delete_user.call_args[0][0].email, "test@example.com")


class TestMedicationsRouter(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    # Add similar test methods for other routers


if __name__ == '__main__':
    unittest.main()

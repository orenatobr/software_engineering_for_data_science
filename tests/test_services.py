# test_services.py - Integration tests for services

import unittest
from unittest.mock import patch

from src.services.database import connect_to_db


class TestDatabase(unittest.TestCase):
    @patch("src.services.database.random.choice", return_value=True)
    def test_connect_to_db(self, mock_random):
        """Test that the database connection function runs without errors."""
        try:
            connect_to_db()
            success = True
        except Exception as e:
            print(f"Database connection failed: {e}")
            success = False

        self.assertTrue(success)


if __name__ == "__main__":
    unittest.main()

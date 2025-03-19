# test_main.py - Unit tests for main.py

import unittest

from src.util import format_response, validate_input


class TestMain(unittest.TestCase):
    def test_validate_input(self):
        self.assertTrue(validate_input(10, int))
        self.assertFalse(validate_input("string", int))

    def test_format_response(self):
        data = {"key": "value"}
        response = format_response(data)
        self.assertEqual(response["status"], "success")
        self.assertEqual(response["data"], data)


if __name__ == "__main__":
    unittest.main()

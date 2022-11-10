
import sys
import unittest
from unittest import mock
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from app.src.services.home.home import homePageService

class TestHome(unittest.TestCase):
    
    @mock.patch("app.src.services.home.home.get")
    def test_homePageService(self, mock_get):

        # Arrange
        mock_get.return_value = {"details": "hello world!"}

        # Act
        get_data = homePageService()

        # Assert
        self.assertDictEqual({"message": "hello world!", "data": None, "status": True}, get_data)
        self.assertEqual("hello world!", get_data["message"])
        self.assertEqual(True, get_data["status"])
        self.assertEqual(None, get_data["data"])
        self.assertIsNotNone(get_data)
        self.assertTrue(get_data)

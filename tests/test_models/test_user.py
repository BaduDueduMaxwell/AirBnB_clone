import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def setUp(self):
        """Set up a User instance for testing."""
        self.user = User()
    
    def test_default_attributes(self):
        """Test default values of User attributes."""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")
    
    def test_set_attributes(self):
        """Test setting and getting User attributes."""
        self.user.email = "test@example.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Doe"

        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
    
    def test_save(self):
        """Test that the save method works."""
        self.user.email = "save@example.com"
        self.user.save()
        
        # Assuming FileStorage is properly set up and used
        from models.engine.file_storage import FileStorage
        storage = FileStorage()
        storage.reload()
        
        # Verify that the user has been saved correctly
        key = f"User.{self.user.id}"
        self.assertIn(key, storage.all())
        saved_user = storage.all()[key]
        self.assertEqual(saved_user.email, "save@example.com")

if __name__ == "__main__":
    unittest.main()

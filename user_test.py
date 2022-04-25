import unittest
from . import User


class TestUser(unittest.TestCase):

    def setUp(self):
        """
        Set up method to run before each test case
        """
        #  create user object
        self.new_user = User("roseline", "test123")

    def test_init(self):
        """ test_init test case to test if new users is instantiated successfully """

        self.assertEqual(self.new_user.username, "roseline")
        self.assertEqual(self.new_user.password, "test123")

    def test_create_user(self):
        """
        test_create_user test case tests whether a new user is created
        """

        self.new_user.create_user()
        self.assertEqual(len(User.user_list), 1)

    def test_delete_user(self):
        """
        Test if we can remove user from User List
        """

        self.new_user.create_user()
        test_user = User("roseline", "password")
        test_user.create_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)

    def test_find_user_by_username(self):
        """Test  find user by username"""

        self.new_user.create_user()
        test_user = User("roseline", "password")
        test_user.create_user()

        found_user = User.find_by_username("roseline")

        self.assertEqual(found_user.password, test_user.password)


if __name__ == '__main__':
    unittest.main()

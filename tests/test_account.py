import unittest
from app.models.account import User


class AccountTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User("calvinpete", "pass12", "tinkacalvin@gmail.com", "LF")

    def test_existence(self):
        self.assertIsInstance(self.user, User)

    def test_validate_email_address(self):
        self.assertEqual(self.user.validate_email_address(), True)


if __name__ == "__main__":
    unittest.main()

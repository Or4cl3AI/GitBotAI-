```python
import unittest
from GitBotAI.authentication import authenticate_user

class TestAuthentication(unittest.TestCase):

    def setUp(self):
        self.valid_token = "valid_token"
        self.invalid_token = "invalid_token"

    def test_authenticate_user_valid_token(self):
        result = authenticate_user(self.valid_token)
        self.assertEqual(result, "AUTH_SUCCESS")

    def test_authenticate_user_invalid_token(self):
        result = authenticate_user(self.invalid_token)
        self.assertNotEqual(result, "AUTH_SUCCESS")

if __name__ == '__main__':
    unittest.main()
```
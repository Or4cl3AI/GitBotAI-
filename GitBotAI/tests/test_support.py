```python
import unittest
from GitBotAI import support

class TestSupport(unittest.TestCase):

    def setUp(self):
        self.user = {
            "username": "test_user",
            "email": "test_user@example.com"
        }

    def test_provide_support(self):
        response = support.provide_support(self.user, "I need help with repository creation")
        self.assertIsNotNone(response)
        self.assertIn('message', response)

    def test_provide_support_no_user(self):
        response = support.provide_support(None, "I need help with repository creation")
        self.assertIsNotNone(response)
        self.assertIn('error', response)

    def test_provide_support_no_query(self):
        response = support.provide_support(self.user, None)
        self.assertIsNotNone(response)
        self.assertIn('error', response)

if __name__ == '__main__':
    unittest.main()
```
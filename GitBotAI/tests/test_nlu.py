```python
import unittest
from GitBotAI.nlu import parse_intent

class TestNLU(unittest.TestCase):

    def setUp(self):
        self.sample_commands = [
            "create a new repository",
            "generate a Python file",
            "deploy to AWS",
            "merge branch feature1",
            "authenticate user"
        ]

    def test_parse_intent(self):
        for command in self.sample_commands:
            intent = parse_intent(command)
            self.assertIsNotNone(intent, f"Failed to parse intent from command: {command}")

if __name__ == "__main__":
    unittest.main()
```
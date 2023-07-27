```python
import unittest
from unittest.mock import patch
from GitBotAI import repository_management

class TestRepositoryManagement(unittest.TestCase):

    @patch('GitBotAI.repository_management.requests')
    def test_manage_repository(self, mock_requests):
        mock_requests.post.return_value.status_code = 201
        mock_requests.post.return_value.json.return_value = {
            'message': 'REPO_CREATED'
        }

        response = repository_management.manage_repository('test_repo', 'GITHUB_TOKEN')
        self.assertEqual(response, 'REPO_CREATED')

    @patch('GitBotAI.repository_management.requests')
    def test_manage_repository_fail(self, mock_requests):
        mock_requests.post.return_value.status_code = 400
        mock_requests.post.return_value.json.return_value = {
            'message': 'Bad Request'
        }

        response = repository_management.manage_repository('test_repo', 'GITHUB_TOKEN')
        self.assertEqual(response, 'Bad Request')

if __name__ == '__main__':
    unittest.main()
```
```python
import requests
from utils import GITHUB_TOKEN

class Support:
    def __init__(self):
        self.headers = {'Authorization': f'token {GITHUB_TOKEN}'}

    def provide_support(self, user, issue):
        """
        Function to provide support to the user by creating an issue on GitHub
        """
        url = f"https://api.github.com/repos/{user}/GitBotAI/issues"
        issue = {'title': 'User Support Request',
                 'body': issue}
        response = requests.post(url, json=issue, headers=self.headers)

        if response.status_code == 201:
            print('Successfully created Issue: {0}'.format(issue['title']))
        else:
            print('Could not create Issue {0}'.format(issue['title']))
            print('Response:', response.content)

    def get_user_issues(self, user):
        """
        Function to get all issues for a user
        """
        url = f"https://api.github.com/repos/{user}/GitBotAI/issues"
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            issues = response.json()
            for issue in issues:
                print('Issue: {0} - State: {1}'.format(issue['title'], issue['state']))
        else:
            print('Could not get issues for user {0}'.format(user))
            print('Response:', response.content)
```
```python
import requests
from .utils import GITHUB_TOKEN

class RepositoryManager:
    BASE_URL = "https://api.github.com"

    def __init__(self):
        self.headers = {
            "Authorization": f"token {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json",
        }

    def create_repository(self, repo_name):
        url = f"{self.BASE_URL}/user/repos"
        data = {"name": repo_name}
        response = requests.post(url, headers=self.headers, json=data)

        if response.status_code == 201:
            print("REPO_CREATED")
            return response.json()
        else:
            raise Exception("Failed to create repository")

    def get_repository(self, owner, repo_name):
        url = f"{self.BASE_URL}/repos/{owner}/{repo_name}"
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Failed to get repository")

    def manage_repository(self, owner, repo_name, new_settings):
        url = f"{self.BASE_URL}/repos/{owner}/{repo_name}"
        response = requests.patch(url, headers=self.headers, json=new_settings)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Failed to manage repository")

    def track_repository_changes(self, owner, repo_name):
        url = f"{self.BASE_URL}/repos/{owner}/{repo_name}/commits"
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Failed to track repository changes")
```
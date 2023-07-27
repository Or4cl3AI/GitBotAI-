```python
import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

def make_github_request(url, method='GET', data=None):
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    if method == 'GET':
        response = requests.get(url, headers=headers)
    elif method == 'POST':
        response = requests.post(url, headers=headers, json=data)
    elif method == 'PUT':
        response = requests.put(url, headers=headers, json=data)
    elif method == 'DELETE':
        response = requests.delete(url, headers=headers)
    else:
        raise ValueError('Invalid method')
    response.raise_for_status()
    return response.json()

def validate_user(user):
    url = f'https://api.github.com/users/{user}'
    try:
        make_github_request(url)
        return True
    except requests.exceptions.HTTPError as err:
        print(f'Error: {err}')
        return False

def validate_repo(user, repo):
    url = f'https://api.github.com/repos/{user}/{repo}'
    try:
        make_github_request(url)
        return True
    except requests.exceptions.HTTPError as err:
        print(f'Error: {err}')
        return False

def get_repo_details(user, repo):
    url = f'https://api.github.com/repos/{user}/{repo}'
    return make_github_request(url)

def get_user_repos(user):
    url = f'https://api.github.com/users/{user}/repos'
    return make_github_request(url)
```
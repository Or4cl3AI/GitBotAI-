```python
import os
import requests
from flask import request, jsonify

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

class UserSchema:
    def __init__(self, username, token):
        self.username = username
        self.token = token

def authenticate_user():
    auth_token = request.headers.get('Authorization')
    if not auth_token:
        return jsonify({'message': 'Token is missing!'}), 403

    try:
        response = requests.get('https://api.github.com/user', headers={'Authorization': f'token {auth_token}'})
        response.raise_for_status()
        user_data = response.json()
        user = UserSchema(user_data['login'], auth_token)
        return user
    except requests.exceptions.RequestException as e:
        return jsonify({'message': 'Token is invalid!'}), 403

def check_permissions(user, repo_name):
    try:
        response = requests.get(f'https://api.github.com/repos/{user.username}/{repo_name}', headers={'Authorization': f'token {user.token}'})
        response.raise_for_status()
        repo_data = response.json()
        if repo_data['permissions']['push']:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        return False
```
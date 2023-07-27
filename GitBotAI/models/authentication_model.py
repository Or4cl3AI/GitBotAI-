```python
import os
import requests
from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(required=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    token = fields.Str(required=True)

class AuthenticationModel:
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    API_BASE_URL = "https://api.github.com"

    @staticmethod
    def authenticate_user(user_data):
        headers = {"Authorization": f"token {AuthenticationModel.GITHUB_TOKEN}"}
        response = requests.get(f"{AuthenticationModel.API_BASE_URL}/user", headers=headers)

        if response.status_code == 200:
            user_info = response.json()
            user = UserSchema().load({
                "id": user_info["id"],
                "username": user_info["login"],
                "email": user_info["email"],
                "token": AuthenticationModel.GITHUB_TOKEN
            })
            return user
        else:
            raise Exception("Authentication failed")

    @staticmethod
    def check_user_permission(user, repo_name):
        headers = {"Authorization": f"token {user.token}"}
        response = requests.get(f"{AuthenticationModel.API_BASE_URL}/repos/{user.username}/{repo_name}/collaborators/{user.username}/permission", headers=headers)

        if response.status_code == 200:
            permission_data = response.json()
            return permission_data["permission"]
        else:
            raise Exception("Failed to check user permission")
```
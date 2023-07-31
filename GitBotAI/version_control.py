import os
import requests
from .utils import handle_response

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
API_BASE_URL = "https://api.github.com"

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

def create_branch(repo_name, branch_name, commit_sha):
    url = f"{API_BASE_URL}/repos/{repo_name}/git/refs"
    data = {
        "ref": f"refs/heads/{branch_name}",
        "sha": commit_sha
    }
    response = requests.post(url, headers=headers, json=data)
    handle_response(response)

def commit_changes(repo_name, branch_name, message, changes):
    url = f"{API_BASE_URL}/repos/{repo_name}/git/commits"
    data = {
        "message": message,
        "tree": changes,
        "parents": [branch_name]
    }
    response = requests.post(url, headers=headers, json=data)
    handle_response(response)

def merge_branches(repo_name, base_branch, head_branch):
    url = f"{API_BASE_URL}/repos/{repo_name}/merges"
    data = {
        "base": base_branch,
        "head": head_branch
    }
    response = requests.post(url, headers=headers, json=data)
    handle_response(response)

def handle_conflicts(conflict):
    # This is a placeholder function. Conflict handling will depend on the specific requirements of the project.
    pass

def sweep_and_merge_branches(repo_name):
    branches_url = f"{API_BASE_URL}/repos/{repo_name}/branches"
    response = requests.get(branches_url, headers=headers)
    handle_response(response)
    branches = response.json()
    
    main_branch = "main"  # Replace with the actual name of the main branch
    
    for branch in branches:
        branch_name = branch["name"]
        merge_branches(repo_name, main_branch, branch_name)
        # Handle conflicts if any
        handle_conflicts(conflict)

def version_control(repo_name, command, **kwargs):
    if command == "create_branch":
        create_branch(repo_name, kwargs.get("branch_name"), kwargs.get("commit_sha"))
    elif command == "commit_changes":
        commit_changes(repo_name, kwargs.get("branch_name"), kwargs.get("message"), kwargs.get("changes"))
    elif command == "merge_branches":
        merge_branches(repo_name, kwargs.get("base_branch"), kwargs.get("head_branch"))
    elif command == "handle_conflicts":
        handle_conflicts(kwargs.get("conflict"))
    elif command == "sweep_and_merge_branches":
        sweep_and_merge_branches(repo_name)
    else:
        raise ValueError("Invalid command")
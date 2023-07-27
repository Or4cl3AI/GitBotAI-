```python
# GitBotAI/templates/repository_templates.py

# This file contains predefined templates for repository management operations.

# Template for creating a new repository
new_repo_template = {
    "name": None,
    "description": None,
    "private": False,
    "has_issues": True,
    "has_projects": True,
    "has_wiki": True
}

# Template for updating a repository
update_repo_template = {
    "name": None,
    "description": None,
    "private": None,
    "has_issues": None,
    "has_projects": None,
    "has_wiki": None
}

# Template for creating a new branch
new_branch_template = {
    "ref": None,
    "sha": None
}

# Template for creating a new pull request
new_pull_request_template = {
    "title": None,
    "body": None,
    "head": None,
    "base": None
}
```
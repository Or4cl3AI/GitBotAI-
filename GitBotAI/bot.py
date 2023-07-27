```python
import os
from flask import Flask, request
from GitBotAI.code_generation import generate_code
from GitBotAI.deployment import deploy_code
from GitBotAI.repository_management import manage_repository
from GitBotAI.version_control import version_control
from GitBotAI.nlu import parse_intent
from GitBotAI.authentication import authenticate_user
from GitBotAI.documentation import generate_documentation
from GitBotAI.support import provide_support

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    user = authenticate_user(data['user'])
    if not user:
        return {"message": "Authentication failed."}, 401

    intent, entities = parse_intent(data['message'])
    if intent == 'generate_code':
        response = generate_code(entities, user)
    elif intent == 'deploy_code':
        response = deploy_code(entities, user)
    elif intent == 'manage_repository':
        response = manage_repository(entities, user)
    elif intent == 'version_control':
        response = version_control(entities, user)
    elif intent == 'generate_documentation':
        response = generate_documentation(entities, user)
    elif intent == 'provide_support':
        response = provide_support(entities, user)
    else:
        response = {"message": "Invalid command."}

    return response

if __name__ == "__main__":
    app.run(port=int(os.getenv('PORT', 5000)), debug=True)
```
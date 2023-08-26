from flask import Flask, request
from GitBotAI.bot import GitBotAI

app = Flask(__name__)
bot = GitBotAI()

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    bot.handle_update(data)
    return 'ok'

@app.route('/authenticate', methods=['GET'])
def authenticate():
    code = request.args.get('code')
    bot.authenticate_user(code)
    return 'ok'

@app.route('/sweep_and_merge', methods=['POST'])
def sweep_and_merge():
    repo_name = request.form.get('repo_name')
    version_control(repo_name, 'sweep_and_merge_branches')
    return 'ok'

if __name__ == '__main__':
    app.run(port=5000)
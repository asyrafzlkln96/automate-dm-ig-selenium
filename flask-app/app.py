from flask import Flask

app = Flask(__name__)


@app.route('/api/submit')
def automate_dms():
    return 'Hello, World!'

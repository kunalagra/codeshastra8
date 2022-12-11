from flask import Flask
app = Flask(__name__)

from views import *

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

if __name__ == "__main__":
    app.run(debug="true")
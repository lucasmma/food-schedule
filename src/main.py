from flask import Flask

app = Flask(__name__, template_folder='templates')

from routes import *

if __name__ == "__main__":
    app.run(debug=True, port=3000, host='0.0.0.0')

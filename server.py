# Imported flask and jsonify
from flask import Flask, send_from_directory

# Created a Flask app
app = Flask(__name__, static_url_path='')

#######################
# A route handler is a function responding to an HTTP request
# Exp:
#  - A client requests route '/' => http://localhost:5000/
#  - This function is called
#  - The return statement sends the response back to the client
#######################


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)


@app.route('/')
def home():
    return send_from_directory('', 'index.html')

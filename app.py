from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from resource import *

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


@app.route('/addMovie', methods=['POST'])
def add_movie():
    if request.method == 'POST':
        if request.data:
            return add_movie_info(json.loads(request.data))
    else:
        return "Invalid methods, API supports POST method"


@app.route('/addActor', methods=['POST'])
def add_actor():
    if request.method == 'POST':
        if request.data:
            return add_actor_info(json.loads(request.data))
    else:
        return "Invalid methods, API supports POST method"


@app.route('/showMovie', methods=['GET', 'POST'])
def show_movie():
    if request.method in ['POST', 'GET']:
        return jsonify(show_all_movies())
    else:
        return 'Invalid methods'

@app.route('/actorMovie', methods=['GET', 'POST'])
def actor_movie():
    if request.method == 'POST' or request.method == 'GET':
        data = json.loads(request.data)
        return jsonify(get_movies_by_actor_id(data))
    else:
        return 'Invalid methods'

@app.route('/showActor', methods=['GET', 'POST'])
def show_actor():
    if request.method in ['POST', 'GET']:
        return jsonify(show_all_actor())
    else:
        return 'Invalid methods'


@app.route('/showActorById', methods=['POST'])
def show_actor_by_id():
    if request.method == 'POST' or request.method == 'GET':
        data = json.loads(request.data)
        print data
        return  jsonify(get_actor_by_id(data))
    else:
        return 'Invalid methods'


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return "Welcome to Movie selector API"

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
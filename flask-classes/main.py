import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})	# CORS
# CORS(app, resources={r'/*': {'origins': 'http://localhost:8080', "allow_headers": "Access-Contr01-A110w-Origin"}})	# CORS for localhost:8080

@app.route('/api/', methods=['GET'])
def greetings():
    return ("Hello, World!")

@app.route('/api/shark', methods=['GET'])
def shark():
    return ("Shark 🚀")

GAMES = [
    {
        "title": 'Hogwarts Legacy',
        "genre": 'RPG',
        "played": True
    },
    {
        "title": 'Stray',
        "genre": 'Adventure',
        "played": True
    },
    {
        "title": 'Fortinaite',
        "genre": 'battle royale',
        "played": True
    },
    {
        "title": 'Rocket League',
        "genre": 'Soccer',
        "played": True
    },
    {
        "title": "assassin's creed odyssey",
        "genre": 'RPG',
        "played": False
    },
    {
        "title": 'God of war',
        "genre": 'Adventure',
        "played": False
    },
    {
        "title": 'Day z',
        "genre": 'Survival',
        "played": False
    },
    {
        "title": 'Fall Guys',
        "genre": 'battle royale',
        "played": True
    },
]

# The GET route handle
@app.route('/api/games', methods=['GET', 'POST'])
def all_games():
    response_object = {'status':'success'}
    if request.method == "POST":
        post_data = request.get_json()
        GAMES.append({
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played'),
        })
        response_object['message'] = 'Game Added!'
    else :
        response_object['games'] = GAMES
    return jsonify(response_object)

# The PUT and DELETE route handler
@app.route('/api/games/<games_id>', methods=['PUT'])
def single_game(game_id):
    response_object = {'status':'success'}
    if request.method == "PUT":
        post_data = request.get_json()
        GAMES.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played'),
        })
        response_object['message'] = 'Game Updated!'
    return jsonify(response_object)

def remove_game(game_id):
    for game in GAMES:
        if game['id'] == game_id:
            GAMES.remove(game)
            return True
    return False

if __name__ == '__main__':
    app.run(debug=True)
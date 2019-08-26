"""
This is the starting point of the Flask based web application. It exposes
all the necessary HTTP headers GET, PUT, POST, HEAD, DELETE.
"""
from flask import Flask, request
import resources

app = Flask(__name__)

@app.route('/keys', methods=['GET', 'POST', 'DELETE'])
def choreslist():

    if request.method == 'GET':
        return resources.get_chores()

    elif request.method == 'POST':
        chore = request.get_json()
        return resources.make_a_new_chore(chore)

    elif request.method == 'DELETE':
        return resources.delete_all_chores()

@app.route('/keys/<title>', methods=['HEAD', 'PUT', 'DELETE'])
def chores(title):
    if request.method == 'HEAD':
        return resources.get_chore(title)

    elif request.method == 'PUT':
        chore = request.get_json()[title]
        return resources.update_a_chore(title, chore)

    elif request.method == 'DELETE':
        return resources.delete_a_chore(title)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Hello world!"

@app.route("/key/activate/<id_>", methods=["GET"])
def auth(id_):
    isAuth = False
    with open('keys.txt') as keys:
        data = json.load(keys)
        newData = {}
        newData['keys'] = []
        for k in data['keys']:
            newData['keys'].append(k)
            if (k['key'] == id_ and k['code'] == '0'):
                isAuth = True
                newData['keys'][len(newData['keys']) - 1]['code'] = "1"  
    with open('keys.txt', 'w') as keys:
        json.dump(newData, keys)
    return jsonify({'isAuth' : isAuth})


@app.route("/key/deactivate/<id_>", methods=["GET"])
def exit(id_):
    with open('keys.txt') as keys:
        data = json.load(keys)
        newData = {}
        newData['keys'] = []
        for k in data['keys']:
            newData['keys'].append(k)
            if (k['key'] == id_ and k['code'] == '1'):
                newData['keys'][len(newData['keys']) - 1]['code'] = "0"
        with open('keys.txt', 'w') as keys:
            json.dump(newData, keys)
        return jsonify({'status': 'good'})

@app.route("/keys", methods=["GET"])
def keys():
    # line = ''
    with open('keys.txt') as keys:
        data = json.load(keys)
        # for k in data['keys']:
        #     line += k['key'] + ' ' + k['code'] + '<br>'
    return data
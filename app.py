from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
import uuid

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'healthdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/healthdb'

mongo = PyMongo(app)


@app.route('/hosts', methods=['GET'])
def get_all_hosts():
    host = mongo.db.hosts
    output = []
    for s in host.find():
        output.append(s)
    return jsonify({'result': output})


@app.route('/host/', methods=['GET'])
def get_one_host(name):
    host = mongo.db.hosts
    s = host.find_one({'hostname': name})
    if s:
        output = s
    else:
        output = "No such name"
    return jsonify({'result': output})


@app.route('/host/add', methods=['POST'])
def add_host():
    host = mongo.db.hosts
    data = request.json
    existing_id = host.find_one({'hostname': data['hostname']}, {'_id': 1})
    if existing_id is None:
        data.update({'_id': uuid.uuid4().hex})
        host_id = host.insert(data)
    else:
        data.update({'_id': existing_id['_id']})
        retcode = host.update({'hostname': data['hostname']}, data)
        if retcode['updatedExisting'] is True:
            host_id = existing_id['_id']
    new_host = host.find_one({'_id': host_id})
    output = new_host
    return jsonify({'result': output})

if __name__ == '__main__':
    app.run(debug=True)
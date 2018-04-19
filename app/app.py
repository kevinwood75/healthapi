from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
import datetime
import uuid

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'healthdb'
app.config['MONGO_URI'] = 'mongodb://192.168.2.148:27017/healthdb'

mongo = PyMongo(app)


@app.route('/hosts', methods=['GET'])
def get_all_hosts():
    host = mongo.db.hosts
    output = []
    for s in host.find():
        output.append(s)
    return jsonify({'result': output})

@app.route('/woods', methods=['GET'])
def get_all_test():
    output = []
    for host in ['saltmaster2', 'docker01', 'docker02']:
        tmp_dict = { 'hostname': host, 'status': 'ok' }
        output.append(tmp_dict)
    return jsonify({'result': output})
       

@app.route('/host/<string:hname>', methods=['GET'])
def get_one_host(hname):
    host = mongo.db.hosts
    s = host.find_one({'hostname': hname})
    if s:
        output = s
    else:
        output = "No such name"
    return jsonify({'result': output})


@app.route('/host/add', methods=['POST'])
def add_host():
    host = mongo.db.hosts
    data = request.json
    try:
        existing_id = host.find_one({'hostname': data['hostname']}, {'_id': 1})
        data.update({'_id': existing_id['_id']})
        data.update({'date': datetime.datetime.utcnow()})
        retcode = host.update({'hostname': data['hostname']}, data)
        if retcode['updatedExisting'] is True:
            host_id = existing_id['_id']

    except (TypeError, AttributeError):
        data.update({'_id': uuid.uuid4().hex})
        data.update({'date': datetime.datetime.utcnow()})
        host_id = host.insert(data)

    new_host = host.find_one({'_id': host_id})
    output = new_host
    return jsonify({'result': output})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

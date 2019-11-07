#!flask/bin/python3.7
from flask import Flask, jsonify, abort, make_response

app = Flask(__name__)

devices = [
    {
        'id': 1,
        'description': u'Keith\'s Desktop',
        'ip': u'192.168.1.182'
    },
    {
        'id': 2,
        'description': u'Keith\'s Macbook Air',
        'ip': u'192.168.1.15'
    }
]

@app.route('/all_devices', methods=['GET'])
def get_all_devices():
    return jsonify({'all_devices': devices})

@app.route('/device/<int:device_id>', methods=['GET'])
def get_device(device_id):
    device = [device for device in devices if device['id'] == device_id]
    if len(device) == 0:
        abort(404)
    return jsonify({'device': device[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)

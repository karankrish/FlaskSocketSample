from flask import Flask 
from flask_socketio import SocketIO, send , emit
from flask_cors import CORS
import json
app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

@app.route('/<key>', methods=['GET'])
def dataCountuniversity(key):
    data = {"message": key}
    handle_my_custom_event(data)
    return str(data).replace("\'", "\"")
msg="asd"
@socketio.on('message')
def handleMessage():
    print('Message: ' )
    data = json.loads({"message": "asd"})
    send(str(data).replace("\'", "\""), broadcast=True)


j=json.loads('{"data":"ass"}')
'''
@socketio.on('res')
def handle_my_custom_event(j):
    emit('my response', j,broadcast=True)
'''

if __name__ == '__main__':
	socketio.run(app,host="192.168.100.20",port=7555)

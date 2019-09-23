
from flask import Flask
from flask_socketio import SocketIO, send , emit
from flask_cors import CORS
'''
import eventlet
eventlet.monkey_patch()
from gevent import monkey
monkey.patch_all()
'''
app = Flask(__name__)
app.config["INFO"] = True
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app,message_queue='amqp://user:bitnami@localhost:5672')
socketio.init_app(app, cors_allowed_origins="*")

@socketio.on('connection')
def handleMessage():
    socketio = SocketIO(message_queue='amqp://user:bitnami@localhost:5672')
    socketio.emit('testEmit', "hii")




if __name__ == '__main__':
	socketio.run(app,host="192.168.100.20",port=7444)

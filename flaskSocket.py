from flask import Flask
from flask_socketio import SocketIO, send , emit
from flask_cors import CORS

app = Flask(__name__)
app.config["INFO"] = True
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

def some_function():
    print("===============")
    socketio = SocketIO(message_queue='amqp://user:bitnami@localhost:5672')
    socketio.emit('testEmit', "hiii...")


@socketio.on('connection')
def handleMessage(asd):
    some_function()


@socketio.on('message')
def handleMessage1(asd):
    print('Message: ' +asd)
    send(asd, broadcast=True)

@socketio.on('test')
def handle(asd):
    print('Message: ' +asd)
    
        


if __name__ == '__main__':
	socketio.run(app,host="192.168.100.20",port=7444)

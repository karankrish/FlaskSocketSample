from flask import Flask 
from flask_socketio import SocketIO, send , emit
from flask_cors import CORS

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")


@socketio.on('test')
def handleMessage(asd):
    print('Message: ' +asd)
    send(asd, broadcast=True)
    
def some_function():
    print("===============")
    socketio.emit('testEmit', "hiii...")


some_function()
if __name__ == '__main__':
	socketio.run(app,host="192.168.100.20",port=7444)

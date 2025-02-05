from os import environ
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def home():
    return render_template('index.html')
    
@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my connection', {'data': 'Connected'})
    socketio.send

@socketio.on('my new message', namespace='/test')
def test_message(message):
    # print(f"Message: {message['somethingElse']}")
    emit('new message', {'data': message['data']})
    
    
if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    PORT = int(environ.get('SERVER_PORT', '5000'))
    socketio.run(app, host=HOST, port=PORT, debug=True)
    
    
# Adding code that interfaces with that new SecretPython.py file At some point
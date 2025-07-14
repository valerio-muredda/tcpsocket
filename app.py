import os
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
# Configure SocketIO for production with eventlet or gevent
# Use a secret key for session management (important for production)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'a_default_secret_key_for_dev')
socketio = SocketIO(app, async_mode='eventlet', cors_allowed_origins="*") # Allow all origins for simplicity in demo

@app.route('/')
def index():
    """Serve the main HTML page."""
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    """Handle new client connections."""
    print('Client connected')
    emit('message', {'data': 'Connected to WebSocket server!'})

@socketio.on('disconnect')
def test_disconnect():
    """Handle client disconnections."""
    print('Client disconnected')

@socketio.on('message')
def handle_message(data):
    """Handle incoming messages from clients and echo them back."""
    print(f'Received message: {data}')
    emit('message', {'data': f'Server received: {data}'})

if __name__ == '__main__':
    # Use eventlet for production-ready SocketIO server
    # For development, you might run with `flask run` or `python app.py`
    # In OpenShift, Gunicorn will likely manage this.
    socketio.run(app, host='0.0.0.0', port=5000)

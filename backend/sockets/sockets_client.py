import logging
import socketio

sio = socketio.Client()

logger = logging.getLogger(__name__)

@sio.event
def connect():
    logger.debug('Connected to WebSocket server')

@sio.event
def disconnect():
    logger.debug('Disconnected from WebSocket server')

@sio.event
def response(data):
    logger.debug(f'Received response from WebSocket server: {data}')

def send_message_to_websocket_server(message):
    sio.emit('message', message)

if __name__ == '__main__':
    sio.connect('ws://websocket:8765')

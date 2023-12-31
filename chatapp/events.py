"""
routes module contain the routes for different functionalities.
"""
from .module_chat import get_chat_response
from .extensions import socketio

@socketio.on("connect")
def handle_connect():
    """
    method print the message on console when a client is connected.

    Parameters:
    ----------
    None

    Return:
    ------
    None.

    """
    print("Client connected!")

@socketio.on("new_message")
def handle_new_message(message: str, methods = ['GET', 'POST'])-> str:
    """
    method will take a message from socket.emit method.

    Parameters:
    ----------
    None

    Return:
    ------
    message_response: str
        return the message return by the model.
    """
    # my_message = "Hard code message"
    print(get_chat_response(message))
    socketio.emit("chat", get_chat_response(message))

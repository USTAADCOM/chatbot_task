"""
Application basic configuration module.
"""
import pickle
from flask import Flask
from .events import socketio
from .routes import main

model_m = pickle.load(open('model_GPT2.pkl','rb'))
model_tokenizer = pickle.load(open('tokenizer_GPT2.pkl','rb'))

def create_app():
    """
    method perform the basic configuration for the application.

    Parameters:
    ----------
    None

    Return:
    ------
    app    
        return the app object.
    """
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = "secret"
    app.register_blueprint(main)
    socketio.init_app(app)
    return app

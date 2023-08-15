"""
Main application module which will execute the appllication.
"""
import pickle
from chatapp import create_app, socketio

model_m = pickle.load(open('model_GPT2.pkl','rb'))
model_tokenizer = pickle.load(open('tokenizer_GPT2.pkl','rb'))
app = create_app()
socketio.run(app, debug = True)

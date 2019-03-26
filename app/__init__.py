from flask import Flask

app = Flask(__name__) # instancia da classe Flask

from app.controllers import default

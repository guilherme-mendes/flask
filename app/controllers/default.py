from flask import render_template
from app import app


@app.route("/index/<user>")
@app.route("/", defaults={"user": None})  # definindo uma rota para a página
def index(user):  # página criada
    return render_template('index.html',
                           user=user)

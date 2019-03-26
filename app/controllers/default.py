from app import app

@app.route("/") # definindo uma rota para a página
def index(): # página criada
    return "Hello World!"

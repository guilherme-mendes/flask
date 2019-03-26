from flask import Flask

app = Flask(__name__) # instancia da classe Flask

@app.route("/") # definindo uma rota para a página
def index(): # página criada
    return "Hello World!"

if __name__ == "__main__":
    app.run()

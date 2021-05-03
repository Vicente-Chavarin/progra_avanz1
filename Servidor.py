import flask

app = flask.Flask(__name__)
app.config['Debug'] = True
@app.route('/', methods=['GET'])
def Servidor():
    return "Nombre de los integrantes!\n Andre Ochoa\n Emilio Trujillo\n Jared Cebreros\n Viceente Chavarin"
app.run()
import flask

app = flask.Flask(__name__)
app.config['Debug'] = True
@app.route('/', methods=['GET'])
def home():
    return "Ojayo mina-san!"

app.run()
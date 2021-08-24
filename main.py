from flask import Flask, request, jsonify

from calculadora import calcular

app = Flask(__name__)


@app.route('/')
def index():
    return "Ola Mundo!"


@app.route('/calcular/<texto>', methods=['GET'])
def calculadora(texto):
    return "calculei: %i" % calcular(texto)


@app.route('/calcular/', methods=['POST'])
def calculadora_json():
    content = request.json
    texto = content['texto']
    # ToDo: Tratamento de erros
    resultado = calcular(texto)
    saida = {
        "calculei": resultado
    }
    return jsonify(saida)


app.run(host='0.0.0.0', port=81)

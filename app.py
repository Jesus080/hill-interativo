from flask import Flask, render_template, jsonify
from hillinte import i_hill_climbing, evalua_ruta, coord

app = Flask(__name__)

@app.route('/')
def index():
    ruta = i_hill_climbing()
    distancia = evalua_ruta(ruta)
    return render_template('index.html', ruta=ruta, distancia=distancia)

@app.route('/nueva-ruta', methods=['GET'])
def nueva_ruta():
    ruta = i_hill_climbing()
    distancia = evalua_ruta(ruta)
    return jsonify({'ruta': ruta, 'distancia': distancia})

if __name__ == '__main__':
    app.run(debug=True)
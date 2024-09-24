from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/documentacao')
def documentacao():
    return render_template('documentacao.html')

@app.route('/documentacao/microservicos')
def microservicos():
    return render_template('microservicos.html')

@app.route('/documentacao/gateway')
def gateway():
    return render_template('gateway.html')

@app.route('/documentacao/api')
def api():
    return render_template('api.html')

@app.route('/modulos')
def modulos():
    return render_template('modulos.html')

@app.route('/modulos/cpp')
def cpp():
    return render_template('cpp.html')

@app.route('/modulos/python')
def python():
    return render_template('python.html')

@app.route('/modulos/java')
def java():
    return render_template('java.html')

@app.route('/modulos/redes')
def redes():
    return render_template('redes.html')

@app.route('/modulos/banco-de-dados')
def banco_de_dados():
    return render_template('banco_de_dados.html')

@app.route('/modulos/processamento')
def processamento():
    return render_template('processamento.html')

@app.route('/interface')
def interface():
    return render_template('interface.html')

if __name__ == '__main__':
    app.run(debug=True)
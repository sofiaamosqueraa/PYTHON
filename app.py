from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/projeito')
def projeito():
    return render_template('projeito/projeito.html')

@app.route('/documentacao')
def documentacao():
    return render_template('documentacao/documentacao.html')

@app.route('/documentacao/microservicos')
def microservicos():
    return render_template('documentacao/microservicos.html')

@app.route('/documentacao/gateway')
def gateway():
    return render_template('documentacao/gateway.html')

@app.route('/documentacao/api')
def api():
    return render_template('documentacao/api.html')

@app.route('/modulos')
def modulos():
    return render_template('modulos/modulos.html')

@app.route('/modulos/cpp')
def cpp():
    return render_template('modulos/cpp.html')

@app.route('/modulos/python')
def python():
    return render_template('modulos/python.html')

@app.route('/modulos/java')
def java():
    return render_template('modulos/java.html')

@app.route('/modulos/redes')
def redes():
    return render_template('modulos/redes.html')

@app.route('/modulos/banco-de-dados')
def banco_de_dados():
    return render_template('modulos/banco_de_dados.html')

@app.route('/modulos/processamento')
def processamento():
    return render_template('modulos/processamento.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, rendertemplate

app = Flask(name)

@app.route('/')
def microservices_doc():
def home():
    return rendertemplate('home.html')

@app.route('/documentacao')
def documentacao():
    return rendertemplate('documentacao/documentacao.html')

@app.route('/documentacao/microservicos')
def microservicos():
    return rendertemplate('documentacao/microservicos.html')

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

if __name == '__main':
    app.run(debug=True)
    return render_template('documentacao/microservicos.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/documentacao/microservicos')
def documentacao_microservicos():
    return render_template('documentacao/microservicos.html')

@app.route('/documentacao/gateway')
def documentacao_gateway():
    return render_template('documentacao/gateway.html')

@app.route('/documentacao/api')
def documentacao_api():
    return render_template('documentacao/api.html')

@app.route('/modulos/cplusplus')
def modulos_cplusplus():
    return render_template('modulos/cplusplus.html')

@app.route('/modulos/python')
def modulos_python():
    return render_template('modulos/python.html')

@app.route('/modulos/java')
def modulos_java():
    return render_template('modulos/java.html')

@app.route('/modulos/administracao_redes_locais')
def modulos_administracao_redes_locais():
    return render_template('modulos/administracao_redes_locais.html')

@app.route('/modulos/base_de_dados')
def modulos_base_de_dados():
    return render_template('modulos/base_de_dados.html')

@app.route('/modulos/processamento_computacional')
def modulos_processamento_computacional():
    return render_template('modulos/processamento_computacional.html')

@app.route('/interface_projeto')
def interface_projeto():
    return render_template('interface_projeto.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/documentacao', methods=['GET', 'POST'])
def documentacao():
    section_to_show = request.args.get('section')  # Não define um padrão
    return render_template('documentacao.html', section=section_to_show)

@app.route('/modulos')
def modulos():
    return render_template('modulos.html')

@app.route('/projeto')
def projeto():
    return render_template('projeto.html')

@app.route('/modulo/<nome>')
def modulo(nome):
    return render_template('modulos.html', modulo=nome)

if __name__ == '__main__':
    app.run(debug=True)
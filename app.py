from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/documentacao')
def documentacao():
    return render_template('documentacao.html')

@app.route('/modulos')
def modulos():
    return render_template('modulos.html')

@app.route('/projeto')
def projeto():
    return render_template('projeto.html')

if __name__ == '__main__':
    app.run(debug=True)

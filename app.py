from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def microservices_doc():
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

if __name__ == '__main__':
    app.run(debug=True)
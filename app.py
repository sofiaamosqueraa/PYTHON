from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
<<<<<<< HEAD
def microservices_doc():
=======
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
>>>>>>> 274c5190c9e59d6c3a711c147061f6fcc3bc41ba
    return render_template('documentacao/microservicos.html')

if __name__ == '__main__':
    app.run(debug=True)
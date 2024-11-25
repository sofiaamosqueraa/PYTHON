<<<<<<< HEAD
from flask import Flask, render_template
=======
from flask import Flask, render_template, request
>>>>>>> 781f514bae633f516a2795f644e735cfb2d90a1c

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

<<<<<<< HEAD
@app.route('/documentacao')
def documentacao():
    return render_template('documentacao.html')
=======
@app.route('/documentacao', methods=['GET', 'POST'])
def documentacao():
    section_to_show = request.args.get('section')  # Não define um padrão
    return render_template('documentacao.html', section=section_to_show)
>>>>>>> 781f514bae633f516a2795f644e735cfb2d90a1c

@app.route('/modulos')
def modulos():
    return render_template('modulos.html')

@app.route('/projeto')
def projeto():
    return render_template('projeto.html')

if __name__ == '__main__':
    app.run(debug=True)

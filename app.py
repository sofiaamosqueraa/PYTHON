from flask import Flask, render_template, request
from calculadora import app as calculadora_app
from simulador import executar

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/documentacao', methods=['GET', 'POST'])
def documentacao():
    section_to_show = request.args.get('section')  # Não define um padrão
    return render_template('documentacao.html', section=section_to_show)

@app.route('/projeto')
def projeto():
    return render_template('projeto.html')

@app.route('/modulos', methods=['GET'])
def modulos():
    modulo = request.args.get('modulo')  # Obtém o módulo selecionado
    return render_template('modulos.html', modulo=modulo)
    
@app.route('/teste', methods=['GET', 'POST'])
def teste():
    calc_resultado = None
    sim_resultado = None
    
    if request.method == 'POST':
        if 'calcular' in request.form:
            operacao = request.form['operacao']
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            
            response = calculadora_app.test_client().post('/calcular', json={
                'operacao': operacao,
                'num1': num1,
                'num2': num2
            })
            
            if response.status_code == 200:
                calc_resultado = response.get_json().get('resultado')
            else:
                calc_resultado = response.get_json().get('erro')
        
        elif 'executar' in request.form:
            instrucao = request.form['instrucao']
            operandos = request.form['operandos'].split(',')
            operandos = [op.strip() for op in operandos]  # Remove espaços em branco

            # Chama a função do simulador
            sim_resultado = executar(instrucao, operandos)

    return render_template('teste.html', calc_resultado=calc_resultado, sim_resultado=sim_resultado)

if __name__ == '__main__':
    app.run(debug=True)
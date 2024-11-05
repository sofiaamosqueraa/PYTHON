from flask import Flask, render_template, request
import time

app = Flask(__name__)

# Rota principal
@app.route('/')
def home():
    return render_template('home.html')

# Rota para cada página (sem mudanças)
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
    return render_template('modulos/processamento/index.html')

@app.route('/modulos/processamento/organizacao')
def processamento_organizacao():
    return render_template('modulos/processamento/organizacao.html')

@app.route('/modulos/processamento/componentes')
def processamento_componentes():
    return render_template('modulos/processamento/componentes.html')

# Rota para a página de memória com a calculadora
@app.route('/modulos/processamento/memoria')
def processamento_memoria():
    return render_template('modulos/processamento/memoria.html')


# Rota para o processador
@app.route('/modulos/processamento/processador', methods=['GET', 'POST'])
def processamento_processador():
    passos = []
    resultado = None

    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operacao = request.form['operacao']

        # Simular busca
        passos.append("Buscando instrução...")
        time.sleep(1)

        # Simular decodificação
        passos.append("Decodificando operação...")
        time.sleep(1)

        # Simular execução
        passos.append("Executando cálculo...")
        time.sleep(1)

        # Operações permitidas
        operacoes_permitidas = ['+', '-', '*', '/', '&', '|']
        if operacao not in operacoes_permitidas:
            resultado = 'Operação não permitida'
        else:
            if operacao == '/' and num2 == 0:
                resultado = 'Divisão por zero não é permitida'
            else:
                if operacao in ['&', '|']:
                    resultado = eval(f'int({num1}) {operacao} int({num2})')
                else:
                    resultado = eval(f'{num1} {operacao} {num2}')

        passos.append(f"Resultado: {resultado}")

    return render_template('modulos/processamento/processador.html', resultado=resultado, passos=passos)


if __name__ == '__main__':
    app.run(debug=True)

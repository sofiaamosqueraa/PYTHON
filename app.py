from flask import Flask, render_template, request, jsonify

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
@app.route('/modulos/processamento/processador')
def processamento_processador():
    return render_template('modulos/processamento/processador.html')

# Simulação de operações básicas (sem alterações)
@app.route('/simular', methods=['POST'])
def simular():
    try:
        dados = request.get_json()
        
        # Validação de dados
        if not all(key in dados for key in ['num1', 'num2', 'operacao']):
            return jsonify({
                'status': 'error',
                'mensagem': 'Dados incompletos'
            }), 400
        
        num1 = float(dados['num1'])
        num2 = float(dados['num2'])
        operacao = dados['operacao']
        
        # Operações permitidas
        operacoes_permitidas = ['+', '-', '*', '/', '&', '|']
        if operacao not in operacoes_permitidas:
            return jsonify({
                'status': 'error',
                'mensagem': 'Operação não permitida'
            }), 400
            
        # Evitar divisão por zero
        if operacao == '/' and num2 == 0:
            return jsonify({
                'status': 'error',
                'mensagem': 'Divisão por zero não é permitida'
            }), 400
            
        # Calcular resultado
        if operacao in ['&', '|']:
            resultado = eval(f'int({num1}) {operacao} int({num2})')
        else:
            resultado = eval(f'{num1} {operacao} {num2}')
            
        return jsonify({
            'status': 'success',
            'resultado': resultado
        })
        
    except ValueError:
        return jsonify({
            'status': 'error',
            'mensagem': 'Valores inválidos'
        }), 400
    except Exception as e:
        return jsonify({
            'status': 'error',
            'mensagem': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify

app = Flask(__name__)

# Funções da calculadora
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b if b != 0 else 'Erro: Divisão por zero'


@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.json
    operacao = data.get('operacao')
    num1 = data.get('num1')
    num2 = data.get('num2')

    operacoes = {
        'soma': soma,
        'subtracao': subtracao,
        'multiplicacao': multiplicacao,
        'divisao': divisao
    }

    if operacao in operacoes:
        resultado = operacoes[operacao](num1, num2)
    else:
        return jsonify({'erro': 'Operação inválida'}), 400

    return jsonify({'resultado': resultado})



if __name__ == '__main__':
    app.run(port=5000)
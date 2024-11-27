# simulador.py
# Estado do processador
registradores = {'AX': 0, 'BX': 0, 'CX': 0, 'DX': 0}
pc = 0
flags = {'zero': False, 'carry': False, 'overflow': False}

def executar(instrucao, operandos):
    global registradores, pc, flags
    
    resultado = None
    erro = None

    if instrucao == 'MOV':
        destino, valor = operandos
        if destino in registradores:
            registradores[destino] = int(valor)
        else:
            erro = f"Registrador {destino} não existe"
    elif instrucao == 'ADD':
        # Verifica se todos os operandos são registradores válidos
        if all(op in registradores for op in operandos):
            resultado = sum(registradores[op] for op in operandos)  # Soma todos os registradores
            # Atualiza o primeiro registrador com o resultado
            registradores[operandos[0]] = resultado
            flags['zero'] = (resultado == 0)
            flags['carry'] = (resultado > 65535)
        else:
            erro = "Um ou mais registradores inválidos"

    pc += 1

    return {
        'resultado': resultado,
        'registradores': registradores,
        'pc': pc,
        'erro': erro
    }
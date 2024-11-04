// Simulador de processamento
async function simular() {
    const num1 = document.getElementById('num1').value;
    const num2 = document.getElementById('num2').value;
    const operacao = document.getElementById('operacao').value;
    
    if (!num1 || !num2) {
        alert('Por favor, preencha ambos os números');
        return;
    }
    
    const steps = document.querySelectorAll('.step');
    steps.forEach(step => step.classList.remove('active'));
    
    // Simular cada etapa do processamento
    await simularEtapa('busca', 'Buscando instrução...', 1000);
    await simularEtapa('decodificacao', 'Decodificando operação...', 1000);
    await simularEtapa('execucao', 'Executando cálculo...', 1000);
    
    // Calcular e mostrar resultado
    try {
        let resultado;
        if (operacao === '&' || operacao === '|') {
            resultado = eval(`${parseInt(num1)} ${operacao} ${parseInt(num2)}`);
        } else {
            resultado = eval(`${num1} ${operacao} ${num2}`);
        }
        await simularEtapa('resultado', `Resultado: ${resultado}`, 0);
    } catch (error) {
        await simularEtapa('resultado', 'Erro na operação', 0);
    }
}

async function simularEtapa(id, texto, delay) {
    const elemento = document.getElementById(id);
    elemento.textContent = texto;
    elemento.classList.add('active');
    if (delay) {
        await new Promise(resolve => setTimeout(resolve, delay));
    }
}

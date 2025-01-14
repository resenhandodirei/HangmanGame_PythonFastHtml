// Aguarde o carregamento completo do DOM
document.addEventListener("DOMContentLoaded", () => {
    const input = document.querySelector('input[type="text"]');
    const button = document.querySelector('button');
    const message = document.querySelector('.message');

    button.addEventListener('click', () => {
        const guessedLetter = input.value.trim();

        if (guessedLetter === '') {
            message.textContent = 'Por favor, digite uma letra!';
            message.className = 'message error';
            return;
        }

        // Faça algo com a letra digitada (exemplo: enviar para o servidor ou validar localmente)
        console.log(`Letra enviada: ${guessedLetter}`);
        
        // Exemplo de feedback
        if (guessedLetter === 'a') { // Simulação de uma letra correta
            message.textContent = `Parabéns! Você acertou a letra '${guessedLetter}'!`;
            message.className = 'message success';
        } else {
            message.textContent = `Letra '${guessedLetter}' não está correta. Tente novamente!`;
            message.className = 'message error';
        }

        // Limpa o campo de texto
        input.value = '';
    });
});

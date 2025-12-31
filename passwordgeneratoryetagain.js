/**
 * Gera uma senha aleatória segura com base nos parâmetros fornecidos.
 * @param {number} tamanho - Quantidade de caracteres da senha.
 * @param {boolean} incluirEspeciais - Define se terá símbolos (!@#$%...).
 * @returns {string} - A senha gerada.
 */
function gerarSenha(tamanho, incluirEspeciais) {
    const letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    const simbolos = "!@#$%^&*()_+~`|}{[]:;?><,./-=";
    
    // Define o conjunto de caracteres inicial
    let caracteresDisponiveis = letras;
    
    // Adiciona símbolos se o usuário desejar
    if (incluirEspeciais) {
        caracteresDisponiveis += simbolos;
    }

    let senhaFinal = "";
    for (let i = 0; i < tamanho; i++) {
        // Escolhe um índice aleatório dentro do conjunto disponível
        const indiceAleatorio = Math.floor(Math.random() * caracteresDisponiveis.length);
        // Monta a string caractere por caractere
        senhaFinal += caracteresDisponiveis.charAt(indiceAleatorio);
    }

    return senhaFinal;
}

// Exemplo de uso:
const novaSenha = gerarSenha(16, true);
console.log("Sua nova senha segura é: " + novaSenha);

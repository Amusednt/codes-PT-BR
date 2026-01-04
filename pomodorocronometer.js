/**
 * Inicia um temporizador de produtividade (Pomodoro).
 * @param {number} minutosTrabalho - Tempo focado.
 * @param {number} minutosPausa - Tempo de descanso.
 */
function iniciarPomodoro(minutosTrabalho, minutosPausa) {
    let segundosRestantes = minutosTrabalho * 60;
    let emPausa = false;

    console.log(`🚀 Ciclo iniciado! Foco por ${minutosTrabalho} minutos.`);

    // Define um intervalo que roda a cada 1 segundo (1000ms)
    const intervalo = setInterval(() => {
        let min = Math.floor(segundosRestantes / 60);
        let seg = segundosRestantes % 60;

        // Formatação visual (ex: 05:09 em vez de 5:9)
        let display = `${min.toString().padStart(2, '0')}:${seg.toString().padStart(2, '0')}`;
        console.clear(); // Limpa o console para parecer um relógio real
        console.log(emPausa ? "☕ PAUSA:" : "💻 TRABALHO:");
        console.log(display);

        segundosRestantes--;

        // Lógica de troca de ciclo
        if (segundosRestantes < 0) {
            if (!emPausa) {
                console.log("🔔 Hora de descansar!");
                emPausa = true;
                segundosRestantes = minutosPausa * 60;
            } else {
                console.log("🔔 Volta ao trabalho!");
                clearInterval(intervalo); // Encerra após um ciclo completo para exemplo
            }
        }
    }, 1000);
}

// Inicia um ciclo de 25 min de foco e 5 min de pausa
// (Para testar rápido, você pode usar 0.1 e 0.05)
iniciarPomodoro(25, 5);

/**
 * Busca a cotação atual de moedas em relação ao Real (BRL).
 * Utiliza a API pública AwesomeAPI.
 */
async function consultarCambio() {
    const moedas = 'USD-BRL,EUR-BRL,BTC-BRL';
    const url = `https://economia.awesomeapi.com.br/last/${moedas}`;

    console.log("🔄 Consultando cotações atuais...");

    try {
        // Realiza a chamada assíncrona para a API
        const resposta = await fetch(url);
        
        if (!resposta.ok) throw new Error("Erro ao acessar a API");

        const dados = await resposta.json();

        // Itera sobre os resultados e formata a exibição
        Object.values(dados).forEach(moeda => {
            const nome = moeda.name.split('/')[0];
            const valor = parseFloat(moeda.bid).toLocaleString('pt-BR', { 
                style: 'currency', 
                currency: 'BRL' 
            });
            const variacao = moeda.pctChange;

            console.log(`--- ${nome} ---`);
            console.log(`Valor: ${valor}`);
            console.log(`Variação: ${variacao}%`);
        });

    } catch (erro) {
        console.error("❌ Falha na requisição:", erro.message);
    }
}

// Executa a função
consultarCambio();

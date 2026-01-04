import re
from collections import Counter

def analisar_texto(texto):
    """
    Realiza uma análise estatística detalhada de um texto fornecido.
    :param texto: String contendo o texto a ser analisado.
    """
    # Remove pontuação e transforma tudo em minúsculas para contagem justa
    palavras = re.findall(r'\w+', texto.lower())
    
    total_palavras = len(palavras)
    total_caracteres = len(texto)
    
    # Conta a frequência de cada palavra
    frequencia = Counter(palavras)
    
    # Calcula tempo estimado de leitura (média de 200 palavras por minuto)
    tempo_leitura = total_palavras / 200

    print("--- Relatório de Texto ---")
    print(f"Total de Palavras: {total_palavras}")
    print(f"Total de Caracteres: {total_caracteres}")
    print(f"Tempo de leitura estimado: {tempo_leitura:.2f} minuto(s)")
    print("\nPalavras mais comuns:")
    
    # Exibe as 5 palavras que mais aparecem
    for palavra, contagem in frequencia.most_common(5):
        print(f" - {palavra}: {contagem} vezes")

# Exemplo funcional
meu_texto = "O aprendizado de máquina é uma área da inteligência artificial. A inteligência artificial é o futuro."
analisar_texto(meu_texto)

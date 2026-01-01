import re

def eh_palindromo(texto):
    """
    Remove caracteres não alfanuméricos e verifica se a string
    é idêntica ao seu reverso.
    """
    # Converte para minúsculas e remove tudo que não for letra ou número
    texto_limpo = re.sub(r'[^a-zA-Z0-9]', '', texto).lower()
    
    # Compara a string com ela mesma invertida [::-1]
    return texto_limpo == texto_limpo[::-1]

# Lista de testes
frases = [
    "A base do teto desaba",
    "Roma me tem amor",
    "Python não é palíndromo",
    "A cara rajada da jararaca"
]

print("--- Verificador de Palíndromos ---")
for f in frases:
    resultado = "SIM" if eh_palindromo(f) else "NÃO"
    print(f"'{f}' é um palíndromo? {resultado}")

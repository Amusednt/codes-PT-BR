import socket # Biblioteca para conexões de rede
from datetime import datetime

def scanner_de_portas(alvo):
    """
    Tenta conectar em portas específicas de um IP/Host para verificar se estão abertas.
    :param alvo: Endereço IP ou URL (ex: 'google.com' ou '127.0.0.1')
    """
    print("-" * 50)
    print(f"Escaneando alvo: {alvo}")
    print(f"Iniciado em: {str(datetime.now())}")
    print("-" * 50)

    # Lista de portas comuns para testar (HTTP, HTTPS, FTP, SSH, etc)
    portas_comuns = [21, 22, 23, 25, 53, 80, 110, 443, 3306, 8080]

    try:
        for porta in portas_comuns:
            # Cria um socket para conexão IPv4 (AF_INET) usando TCP (SOCK_STREAM)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Define um tempo limite curto para não travar o código
            s.settimeout(0.5)
            
            # Tenta a conexão. connect_ex retorna 0 se a porta estiver aberta
            resultado = s.connect_ex((alvo, porta))
            
            if resultado == 0:
                print(f"Porta {porta}: ABERTA ✅")
            
            s.close() # Fecha o socket após o teste

    except Exception as e:
        print(f"\nErro durante a execução: {e}")
    
    print("-" * 50)
    print("Escaneamento finalizado.")

# Exemplo de uso (Alvo: Localhost)
if __name__ == "__main__":
    scanner_de_portas("127.0.0.1")

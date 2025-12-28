import psutil # Biblioteca para acessar detalhes do sistema
import time   # Para gerenciar os intervalos de atualização
import os     # Para limpar o console

def monitorar_sistema():
    """
    Função principal que coleta e exibe métricas do hardware
    em um loop contínuo até ser interrompido pelo usuário.
    """
    try:
        print("--- Iniciando Monitoramento (Pressione Ctrl+C para parar) ---")
        
        while True:
            # Limpa o console para a atualização parecer estática (funciona em Windows e Linux)
            os.system('cls' if os.name == 'nt' else 'clear')
            
            # Coleta de porcentagem de uso da CPU (intervalo de 1s para precisão)
            uso_cpu = psutil.cpu_percent(interval=1)
            
            # Coleta estatísticas de memória RAM
            memoria = psutil.virtual_memory()
            
            # Coleta estatísticas de uso de Disco Principal
            disco = psutil.disk_usage('/')

            # Exibição formatada dos dados
            print(f"========= STATUS DO SISTEMA =========")
            print(f"Uso de CPU:      [{uso_cpu}%]")
            print(f"Memória RAM:     [{memoria.percent}%] (Usado: {memoria.used // (1024**2)}MB / Total: {memoria.total // (1024**2)}MB)")
            print(f"Espaço em Disco: [{disco.percent}%] (Livre: {disco.free // (1024**3)}GB)")
            print(f"=====================================")
            
            # Aguarda 2 segundos antes da próxima atualização
            time.sleep(2)

    except KeyboardInterrupt:
        # Captura o comando de saída (Ctrl+C) de forma amigável
        print("\nMonitoramento encerrado pelo usuário.")

if __name__ == "__main__":
    # Ponto de entrada do script
    monitorar_sistema()

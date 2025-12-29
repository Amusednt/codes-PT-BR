import os
import shutil

def organizar_diretorio(caminho_pasta):
    # Dicionário mapeando extensões para nomes de pastas
    formatos = {
        'Imagens': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
        'Documentos': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'Videos': ['.mp4', '.mkv', '.mov'],
        'Compactados': ['.zip', '.rar', '.7z'],
        'Executaveis': ['.exe', '.msi']
    }

    # Muda o diretório de trabalho para o caminho especificado
    os.chdir(caminho_pasta)

    # Itera sobre cada arquivo na pasta
    for arquivo in os.listdir():
        if os.path.isfile(arquivo):
            nome, extensao = os.path.splitext(arquivo)
            extensao = extensao.lower()

            # Verifica em qual categoria a extensão se encaixa
            for pasta, ext_lista in formatos.items():
                if extensao in ext_lista:
                    # Cria a pasta se ela não existir
                    if not os.path.exists(pasta):
                        os.makedirs(pasta)
                    
                    # Move o arquivo para a pasta correspondente
                    shutil.move(arquivo, f"{pasta}/{arquivo}")
                    print(f"Movido: {arquivo} -> {pasta}")

if __name__ == "__main__":
    # Substitua pelo caminho da sua pasta de testes
    alvo = "./minha_pasta_baguncada"
    if os.path.exists(alvo):
        organizar_diretorio(alvo)
    else:
        print("Caminho não encontrado. Verifique a variável 'alvo'.")

import os
import shutil

def organizar_pasta(diretorio):
    formatos = {
        "Imagens": [".jpg", ".png", ".jpeg"],
        "Documentos": [".pdf", ".docx", ".txt"],
        "Planilhas": [".csv", ".xlsx"],
    }

    for arquivo in os.listdir(diretorio):
        nome, extensao = os.path.splitext(arquivo)
        for pasta, ext_lista in formatos.items():
            if extensao.lower() in ext_lista:
                caminho_pasta = os.path.join(diretorio, pasta)
                os.makedirs(caminho_pasta, exist_ok=True)
                shutil.move(os.path.join(diretorio, arquivo), os.path.join(caminho_pasta, arquivo))
                print(f"Movido: {arquivo} -> {pasta}")

# Use um caminho de teste
organizar_pasta("./meu_diretorio_teste")

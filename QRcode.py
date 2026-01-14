import qrcode # Biblioteca para gerar o código
import os

def gerar_qr_code(conteudo, nome_arquivo="meu_qrcode.png"):
    """
    Cria uma imagem de QR Code a partir de um texto ou link.
    :param conteudo: Link ou texto que o QR Code deve conter.
    :param nome_arquivo: Nome do arquivo de imagem salvo.
    """
    try:
        # Configuração do QR Code (tamanho, borda e erro)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        qr.add_data(conteudo)
        qr.make(fit=True)

        # Gera a imagem usando a biblioteca Pillow (PIL)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(nome_arquivo)
        
        print(f"✅ QR Code gerado com sucesso: {os.path.abspath(nome_arquivo)}")

    except Exception as e:
        print(f"❌ Erro ao gerar QR Code: {e}")

# Exemplo de uso:
if __name__ == "__main__":
    gerar_qr_code("https://github.com/seu-usuario", "github_link.png")

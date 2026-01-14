import qrcode # Library to generate the code
import os

def generate_qr_code(content, file_name="my_qrcode.png"):
    """
    Creates a QR Code image from a text or link.
    :param content: Link or text to be encoded in the QR Code.
    :param file_name: Name of the saved image file.
    """
    try:
        # QR Code configuration (size, border, and error correction)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        qr.add_data(content)
        qr.make(fit=True)

        # Generates the image using the Pillow (PIL) library
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(file_name)
        
        print(f"✅ QR Code generated successfully: {os.path.abspath(file_name)}")

    except Exception as e:
        print(f"❌ Error generating QR Code: {e}")

# Example usage:
if __name__ == "__main__":
    generate_qr_code("https://github.com/your-user", "github_link.png")

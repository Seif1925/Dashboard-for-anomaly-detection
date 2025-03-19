import qrcode

def generate_qr_code(url, filename="qr_code.png"):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data(url)
    qr.make(fit=True)
    
    # Generate QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image
    img.save(filename)

    print(f"QR code generated for {url} and saved as {filename}")

# Example usage:
generate_qr_code("https://example.com", "example_qr_code.png")

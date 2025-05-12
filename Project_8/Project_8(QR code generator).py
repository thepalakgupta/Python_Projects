import qrcode

def generate_qr(data, filename="qr_code.png"):
    # Create a QR Code object
    qr = qrcode.QRCode(
        version=1,  # Size of the QR code
        box_size=10,  # Size of each box in pixels
        border=4  # Thickness of border (boxes)
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Generate the image
    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    print(f"✅ QR code saved as {filename}")

def main():
    print("🔲 QR Code Generator")
    data = input("Enter text or URL to encode: ")
    filename = input("Enter filename to save (e.g., myqr.png): ") or "qr_code.png"
    generate_qr(data, filename)

# Run the app
main()

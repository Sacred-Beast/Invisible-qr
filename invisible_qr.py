import qrcode
from PIL import Image
from stegano import lsb

# Message to be hidden
hidden_message = "If you reading this, then you are interested in knowing what can I do...."

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(hidden_message)
qr.make(fit=True)

# Create and save the base QR code
qr_img = qr.make_image(fill="black", back_color="white")
# Convert QR code to RGB mode before hiding data
qr_img = qr_img.convert("RGB")
qr_img.save("qr_code.png")


# Hide secret data inside the QR code using Stegano LSB
secret_image = lsb.hide("qr_code.png", hidden_message)
secret_image.save("invisible_qr.png")

print("✅ Invisible QR code generated successfully! Check 'invisible_qr.png'.")

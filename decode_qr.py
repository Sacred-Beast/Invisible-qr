from stegano import lsb

# Extract hidden message from the invisible QR code
def extract_hidden_data():
    try:
        # Load the invisible QR image
        secret_image = "invisible_qr.png"
        
        # Decode the hidden message
        hidden_message = lsb.reveal(secret_image)
        
        if hidden_message:
            print(f"✅ Hidden message found: {hidden_message}")
        else:
            print("❌ No hidden message found in the QR code.")
    
    except Exception as e:
        print(f"⚠️ Error while decoding: {e}")

# Run the extraction
extract_hidden_data()

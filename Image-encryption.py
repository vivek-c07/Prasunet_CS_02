from PIL import Image
import numpy as np

def encrypt_math(input_path, output_path, key):
    # Open the image
    image = Image.open(input_path)
    pixels = np.array(image)
    
    # Apply a simple encryption algorithm
    encrypted_pixels = (pixels + key) % 256
    encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'))
    
    # Save the encrypted image
    encrypted_image.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_math(input_path, output_path, key):
    # Open the encrypted image
    image = Image.open(input_path)
    pixels = np.array(image)
    
    # Apply the decryption algorithm (reverse of encryption)
    decrypted_pixels = (pixels - key) % 256
    decrypted_image = Image.fromarray(decrypted_pixels.astype('uint8'))
    
    # Save the decrypted image
    decrypted_image.save(output_path)
    print(f"Decrypted image saved to {output_path}")

def main():
    # Example usage
    input_image_path = 'verstappen.png'
    encrypted_image_path = 'encrypted.png'
    decrypted_image_path = 'decrypted.png'
    
    # Key for encryption/decryption
    key = 100  # You can choose any integer value here
    
    # Encrypt the image
    encrypt_math(input_image_path, encrypted_image_path, key)
    
    # Decrypt the image
    decrypt_math(encrypted_image_path, decrypted_image_path, key)

if __name__ == "__main__":
    main()

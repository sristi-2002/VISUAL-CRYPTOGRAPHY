from PIL import Image
import numpy as np


def embed_message(image_array, message):
    # Convert the message to a byte array
    message_bytes = message.encode("utf-8")

    # Get the dimensions of the image
    height, width = image_array.shape

    # Embed the message into the LSB (Least Significant Bit) of the image array
    for i, byte in enumerate(message_bytes):
        for j in range(8):  # Iterate over each bit in the byte
            bit = (byte >> j) & 1  # Extract the j-th bit from the byte
            # Embed the bit into the least significant bit of the image pixel
            image_array[i, j] = (
                image_array[i, j] & 254
            ) | bit  # Set the LSB of image pixel to bit

    return image_array


def generate_shares(image_path, num_shares, message):
    # Open and convert the image to grayscale
    original_image = Image.open(image_path).convert("L")
    # Convert the image to a NumPy array
    image_array = np.array(original_image)

    # Get the dimensions of the image
    height, width = image_array.shape

    # Embed the message into the image array
    image_array = embed_message(image_array, message)

    # Initialize a list to store the shares
    shares = []

    # Create num_shares - 1 random binary matrices
    for _ in range(num_shares - 1):
        random_matrix = np.random.randint(0, 256, size=(height, width), dtype=np.uint8)
        shares.append(random_matrix)

    # Compute the last share such that XORing all shares will give the original image with message
    last_share = image_array.copy()
    for share in shares:
        last_share = np.bitwise_xor(last_share, share)
    shares.append(last_share)

    # Save the shares as image files
    for i, share in enumerate(shares):
        share_image = Image.fromarray(share)
        share_image.save(
            f"Project_image_share_{i + 1}.png"
        )  # Save each share as an image file

    print(
        f"{num_shares} shares generated successfully with embedded message: '{message}'."
    )


# Function to take mass message input
def take_mass_message_input():
    message = input("Enter the message to hide in the shares: ")
    return message


# Example usage:
original_image_path = "tiger_new.jpg"  # Ensure this file exists in the directory
num_shares = 5

# Take input for the message to hide in shares
message_to_hide = take_mass_message_input()

# Generate shares with embedded message
generate_shares(original_image_path, num_shares, message_to_hide)


# pic & mas incrpt


# from PIL import Image
# import numpy as np


# def embed_message(image_array, message):
#     # Convert the message to a byte array
#     message_bytes = message.encode("utf-8")

#     # Get the dimensions of the image
#     height, width = image_array.shape

#     # Embed the message into the LSB (Least Significant Bit) of the image array
#     for i, byte in enumerate(message_bytes):
#         for j in range(8):  # Iterate over each bit in the byte
#             bit = (byte >> j) & 1  # Extract the j-th bit from the byte
#             # Embed the bit into the least significant bit of the image pixel
#             image_array[i, j] = (
#                 image_array[i, j] & 254
#             ) | bit  # Set the LSB of image pixel to bit

#     return image_array


# def generate_shares(image_path, num_shares, message):
#     # Open and convert the image to grayscale
#     original_image = Image.open(image_path).convert("L")
#     # Convert the image to a NumPy array
#     image_array = np.array(original_image)

#     # Get the dimensions of the image
#     height, width = image_array.shape

#     # Embed the message into the image array
#     image_array = embed_message(image_array, message)

#     # Initialize a list to store the shares
#     shares = []

#     # Create num_shares - 1 random binary matrices
#     for _ in range(num_shares - 1):
#         random_matrix = np.random.randint(0, 256, size=(height, width), dtype=np.uint8)
#         shares.append(random_matrix)

#     # Compute the last share such that XORing all shares will give the original image with message
#     last_share = image_array.copy()
#     for share in shares:
#         last_share = np.bitwise_xor(last_share, share)
#     shares.append(last_share)

#     # Save the shares as image files
#     for i, share in enumerate(shares):
#         share_image = Image.fromarray(share)
#         share_image.save(
#             f"Project_image_share_{i + 1}.png"
#         )  # Save each share as an image file

#     print(
#         f"{num_shares} shares generated successfully with embedded message: '{message}'."
#     )


# # Example usage:
# original_image_path = "tiger_new.jpg"  # Ensure this file exists in the directory
# num_shares = 5
# message_to_hide = "SUBHA MAHAJAN"

# # Generate shares with embedded message
# generate_shares(original_image_path, num_shares, message_to_hide)


# #  back original_image_path

# from PIL import Image
# import numpy as np


# def generate_shares(image_path, num_shares):
#     # Open and convert the image to grayscale
#     original_image = Image.open(image_path).convert("L")
#     # Convert the image to a NumPy array
#     image_array = np.array(original_image)
#     # Get the dimensions of the image
#     height, width = image_array.shape

#     # Initialize a list to store the shares
#     shares = []

#     # Create num_shares - 1 random binary matrices
#     for _ in range(num_shares - 1):
#         random_matrix = np.random.randint(0, 256, size=(height, width), dtype=np.uint8)
#         shares.append(random_matrix)

#     # Compute the last share such that XORing all shares will give the original image
#     last_share = image_array.copy()
#     for share in shares:
#         last_share = np.bitwise_xor(last_share, share)
#     shares.append(last_share)

#     # Save the shares as image files
#     for i, share in enumerate(shares):
#         share_image = Image.fromarray(share)
#         share_image.save(
#             f"Project_image_share_{i + 1}.png"
#         )  # Save each share as an image file

#     print(f"{num_shares} shares generated successfully.")


# # Example usage:
# original_image_path = "tiger_new.jpg"  # Ensure this file exists in the directory
# num_shares = 5

# # Generate shares
# generate_shares(original_image_path, num_shares)


# from PIL import Image
# import numpy as np


# def generate_shares(image_path, num_shares):
#     # Open and convert the image to grayscale
#     original_image = Image.open(image_path).convert("L")
#     # Convert the image to a NumPy array
#     image_array = np.array(original_image)
#     # Get the dimensions of the image
#     width, height = original_image.size

#     # Initialize a list to store the shares
#     shares = []

#     # Create num_shares random binary matrices
#     for _ in range(num_shares):
#         random_matrix = np.random.randint(2, size=(height, width))
#         shares.append(random_matrix)

#     # Create the shares by combining the binary matrices with the original image
#     for i in range(num_shares):
#         share_array = np.where(
#             shares[i], image_array, 255
#         )  # Use the random matrix and original image
#         share_image = Image.fromarray(share_array.astype(np.uint8))  # Convert to image
#         share_image.save(
#             f"Project_image_share_{i + 1}.jpg"
#         )  # Save each share as an image file

#     print(f"{num_shares} shares generated successfully.")


# # Example usage:
# original_image_path = "tiger_new.jpg"  # Ensure this file exists in the directory
# num_shares = 10

# # Generate shares
# generate_shares(original_image_path, num_shares)


# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes
# from PIL import Image
# import numpy as np


# def encrypt_message(message, key):
#     cipher = AES.new(key, AES.MODE_EAX)
#     ciphertext, tag = cipher.encrypt_and_digest(message.encode("utf-8"))
#     return ciphertext


# def decrypt_message(ciphertext, key):
#     cipher = AES.new(key, AES.MODE_EAX)
#     decrypted_message = cipher.decrypt(ciphertext)
#     return decrypted_message.decode("utf-8")


# def generate_shares(image_path, num_shares, message):
#     # Open the original image
#     original_image = Image.open(image_path)

#     # Convert the image to grayscale
#     original_image = original_image.convert("L")

#     # Convert the image to a NumPy array
#     image_array = np.array(original_image)

#     # Get the dimensions of the image
#     height, width = original_image.size

#     # Generate a random key for encryption
#     encryption_key = get_random_bytes(16)  # 128-bit key for AES

#     # Encrypt the message
#     encrypted_message = encrypt_message(message, encryption_key)

#     # Initialize an array to store the shares
#     shares = []

#     # Create num_shares random binary matrices
#     for _ in range(num_shares):
#         random_matrix = np.random.randint(2, size=(height, width))
#         shares.append(random_matrix)

#     # Create the shares by combining the binary matrices with the encrypted message
#     for i in range(num_shares):
#         share_array = np.where(shares[i], image_array, 255)  # 255 represents white
#         share_image = Image.fromarray(share_array.astype(np.uint8))

#         # Embed the encrypted message in the least significant bit of the image
#         share_image = share_image.point(lambda x: x & 254 | (encrypted_message[i] & 1))

#         share_image.save(
#             f"message_share_{i + 1}.jpg"
#         )  # Save each share as an image file

#     print(f"{num_shares} shares generated successfully.")

#     return encryption_key


# def reconstruct_message(shares_paths, key):
#     # Load each share
#     shares = [Image.open(path).convert("L") for path in shares_paths]


#     # Get dimensions
#     width, height = shares[0].size

#     # Initialize an array to store the reconstructed message
#     reconstructed_message = np.zeros(len(shares), dtype=np.uint8)

#     # Reconstruct the message
#     for i, share in enumerate(shares):
#         share_array = np.array(share)

#         # Extract the encrypted message from the least significant bit
#         encrypted_message = np.bitwise_and(share_array, 1).astype(np.uint8)

#         # Update the reconstructed message
#         reconstructed_message[i] = encrypted_message[0]

#     # Decrypt the message using the key
#     decrypted_message = decrypt_message(reconstructed_message.tobytes(), key)

#     return decrypted_message


# # Example usage:
# original_image_path = "tiger_new.jpg"
# original_message = "Hello, this is a secret message."
# num_shares = 5

# # Generate shares
# encryption_key = generate_shares(original_image_path, num_shares, original_message)

# # Reconstruct the message
# shares_paths = [f"message_share_{i + 1}.jpg" for i in range(num_shares)]
# reconstructed_message = reconstruct_message(shares_paths, encryption_key)

# print("Original Message:", original_message)
# print("Reconstructed Message:", reconstructed_message)

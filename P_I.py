from PIL import Image
import numpy as np


def embed_message(image_array, message):

    # .....................................Convert the message to a byte array................

    message_bytes = message.encode("utf-8")

    # Get the dimensions of the image
    height, width = image_array.shape

    # Embed the message into the LSB (Least Significant Bit) of the image array

    # ..............................................Embed Message Bytes into Image Pixels:.................
    # .......................For each byte in the message, we iterate over its bits.
    # ............................The LSB of each pixel in the image is replaced with each bit from the message byte.

    for i, byte in enumerate(message_bytes):
        for j in range(8):  # Iterate over each bit in the byte
            bit = (byte >> j) & 1  # Extract the j-th bit from the byte
            # Embed the bit into the least significant bit of the image pixel
            image_array[i, j] = (
                image_array[i, j] & 254
            ) | bit  # Set the LSB of image pixel to bit

    return image_array


# .......Open and Convert the Image to Grayscale:
# .......Convert the Image to a NumPy Array:
# .......Embed the Message into the Image Array:


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

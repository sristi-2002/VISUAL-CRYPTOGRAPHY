from PIL import Image
import numpy as np


def extract_message(image_array):
    # Extract the hidden message from the LSB (Least Significant Bit) of the image array
    message_bytes = bytearray()
    for i in range(image_array.shape[0]):
        byte = 0
        for j in range(8):  # Iterate over each bit in the byte
            bit = image_array[i, j] & 1  # Extract the LSB of image pixel
            byte = byte | (
                bit << j
            )  # Set the j-th bit of the byte to the extracted bit
        message_bytes.append(byte)
        # Stop processing when the end of message symbol (null byte) is encountered
        if message_bytes[-1] == 0:
            break

    # Convert bytearray to string
    hidden_message = message_bytes.decode("utf-8")

    return hidden_message.rstrip("\x00")  # Remove trailing null bytes


def reconstruct_image(shares_paths):
    try:
        # Load all shares and convert to NumPy arrays
        shares = [np.array(Image.open(path).convert("L")) for path in shares_paths]

        # Initialize the reconstructed image with the first share
        reconstructed_image = shares[0].copy()

        # XOR all shares together to reconstruct the original image
        for share in shares[1:]:
            reconstructed_image = np.bitwise_xor(reconstructed_image, share)

        return reconstructed_image

    except Exception as e:
        print(f"Error during image reconstruction: {e}")
        return None


# Example usage:
shares_paths = [
    "Project_image_share_1.png",
    "Project_image_share_2.png",
    "Project_image_share_3.png",
    "Project_image_share_4.png",
    "Project_image_share_5.png",
]

# Reconstruct the image
reconstructed_image = reconstruct_image(shares_paths)

if reconstructed_image is not None:
    # Extract the hidden message from the reconstructed image
    hidden_message = extract_message(reconstructed_image)

    # Save the reconstructed image as "reconstructed.png"
    Image.fromarray(reconstructed_image.astype(np.uint8)).save("constructed.png")
    print("Reconstructed image saved as 'constructed.png'.")
    print("Hidden Message:", hidden_message)
else:
    print("Failed to reconstruct the image.")

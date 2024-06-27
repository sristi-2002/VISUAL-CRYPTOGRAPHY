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
        # Load the shares
        shares = [np.array(Image.open(path).convert("L")) for path in shares_paths]

        # Print shape and type of loaded shares for debugging
        for i, share in enumerate(shares):
            print(f"Share {i+1}: Shape={share.shape}, Type={share.dtype}")

        # Initialize the reconstructed image with the first share
        reconstructed_image = shares[0].copy()

        # XOR all shares together to reconstruct the original image
        for share in shares[1:]:
            reconstructed_image = np.bitwise_xor(reconstructed_image, share)

        # Print shape and type of reconstructed image for debugging
        print(
            f"Reconstructed Image: Shape={reconstructed_image.shape}, Type={reconstructed_image.dtype}"
        )

        # Extract the hidden message from the reconstructed image
        hidden_message = extract_message(reconstructed_image)

        return hidden_message

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
hidden_message = reconstruct_image(shares_paths)

if hidden_message:
    print("Hidden Message:", hidden_message)
else:
    print("Failed to reconstruct the image or extract the message.")


# #  decrpt  mass


# from PIL import Image
# import numpy as np


# def extract_message(image_array):
#     # Extract the hidden message from the LSB (Least Significant Bit) of the image array
#     message_bytes = bytearray()
#     for i in range(image_array.shape[0]):
#         byte = 0
#         for j in range(8):  # Iterate over each bit in the byte
#             bit = image_array[i, j] & 1  # Extract the LSB of image pixel
#             byte = byte | (
#                 bit << j
#             )  # Set the j-th bit of the byte to the extracted bit
#         message_bytes.append(byte)
#         # Stop processing when the end of message symbol (null byte) is encountered
#         if message_bytes[-1] == 0:
#             break

#     # Convert bytearray to string
#     hidden_message = message_bytes.decode("utf-8")

#     return hidden_message.rstrip("\x00")  # Remove trailing null bytes


# def reconstruct_image(shares_paths):
#     # Load the shares
#     shares = [np.array(Image.open(path).convert("L")) for path in shares_paths]

#     # Initialize the reconstructed image with the first share
#     reconstructed_image = shares[0].copy()

#     # XOR all shares together to reconstruct the original image
#     for share in shares[1:]:
#         reconstructed_image = np.bitwise_xor(reconstructed_image, share)

#     # Extract the hidden message from the reconstructed image
#     hidden_message = extract_message(reconstructed_image)

#     return hidden_message


# # Example usage:
# shares_paths = [
#     "Project_image_share_1.png",
#     "Project_image_share_2.png",
#     "Project_image_share_3.png",
#     "Project_image_share_4.png",
#     "Project_image_share_5.png",
# ]
# hidden_message = reconstruct_image(shares_paths)

# print("Hidden Message:", hidden_message)


# orginal

# from PIL import Image
# import numpy as np


# def reconstruct_image(shares_paths):
#     # Load the shares
#     shares = [np.array(Image.open(path).convert("L")) for path in shares_paths]

#     # Initialize the reconstructed image with the first share
#     reconstructed_image = shares[0].copy()

#     # XOR all shares together to reconstruct the original image
#     for share in shares[1:]:
#         reconstructed_image = np.bitwise_xor(reconstructed_image, share)

#     # Convert the NumPy array back to an image
#     reconstructed_image = Image.fromarray(reconstructed_image)
#     return reconstructed_image


# # Example usage:
# shares_paths = [f"Project_image_share_{i + 1}.png" for i in range(5)]
# reconstructed_image = reconstruct_image(shares_paths)

# # Show the reconstructed image (for testing purposes)
# reconstructed_image.show()

# # Save the reconstructed image (optional)
# reconstructed_image.save("reconstructed_image.png")

# print("Image reconstructed successfully.")


# from PIL import Image
# import numpy as np


# def reconstruct_image(shares_paths):
#     # Load the shares
#     shares = [np.array(Image.open(path).convert("L")) for path in shares_paths]

#     # Initialize the reconstructed image with the first share
#     reconstructed_image = shares[0].copy()

#     # XOR all shares together to reconstruct the original image
#     for share in shares[1:]:
#         reconstructed_image = np.bitwise_xor(reconstructed_image, share)

#     # Convert the NumPy array back to an image
#     reconstructed_image = Image.fromarray(reconstructed_image)
#     return reconstructed_image


# # Example usage:
# shares_paths = [f"Project_image_share_{i + 1}.jpg" for i in range(10)]
# reconstructed_image = reconstruct_image(shares_paths)

# # Show the reconstructed image (for testing purposes)
# reconstructed_image.show()

# # Save the reconstructed image (optional)
# reconstructed_image.save("reconstructed_image.jpg")

# print("Image reconstructed successfully.")

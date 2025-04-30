```python
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import os

def send_encrypted(channel, message):
    """
    Encrypts the message using DES and sends it over the channel.

    Args:
        channel: The channel to send the encrypted message over (e.g., a socket).
        message: The message to be encrypted and sent (bytes).
    """

    # Generate a random 8-byte key (DES requires a 64-bit key)
    key = os.urandom(8)  # Use a cryptographically secure random number generator

    # Create a DES cipher object in ECB mode (for simplicity, but ECB is insecure in practice)
    cipher = DES.new(key, DES.MODE_ECB)

    # Pad the message to a multiple of the block size (8 bytes for DES)
    padded_message = pad(message, DES.block_size)

    # Encrypt the padded message
    encrypted_message = cipher.encrypt(padded_message)

    # Send the key and the encrypted message over the channel
    channel.send(key)  # Send
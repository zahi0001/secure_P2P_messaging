from Crypto.Cipher import DES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes


def pad_message(message, block_size=8):
    padding_length = block_size - (len(message) % block_size)
    padding = bytes([padding_length] * padding_length)
    return message.encode() + padding

def unpad_message(padded_message):
    padding_length = padded_message[-1]
    return padded_message[:-padding_length].decode()


def generate_key(password, salt=b'secure_salt', dk_len=8):
   return PBKDF2(password, salt, dkLen=dk_len)

def encrypt_message(message, key):
    cipher = DES.new(key, DES.MODE_CBC)
    iv = cipher.iv
    padded_message = pad_message(message) 
    ciphertext = cipher.encrypt(padded_message)
    return iv + ciphertext 

def decrypt_message(data, key):
    iv, ciphertext = data[:8], data[8:] 
    cipher = DES.new(key, DES.MODE_CBC, iv=iv)
    padded_message = cipher.decrypt(ciphertext)
    return unpad_message(padded_message) 


#import hashlib
import base64

from Crypto import Random
from Crypto.Cipher import AES

import g

class AESCrypto:
    def __init__(self, key):
        self.block_size = 32
        #self.key = hashlib.sha256(key.encode()).digest()
        self.key = key

    def pad(self, str_):
        padding = self.block_size - (len(str_) % self.block_size)
        return str_ + (padding * chr(padding))

    @classmethod
    def unpad(cls, str_):
        return str_[:-ord(str_[len(str_) - 1:])]

    def encrypt(self, plain):
        plain = self.pad(plain)
        e_iv = Random.new().read(AES.block_size)
        aes = AES.new(self.key, AES.MODE_CBC, e_iv)
        return base64.b64encode(e_iv + aes.encrypt(plain))

    def decrypt(self, encoded):
        decoded = base64.b64decode(encoded)
        d_iv = decoded[:16]
        aes = AES.new(self.key, AES.MODE_CBC, d_iv)
        return self.unpad(aes.decrypt(decoded[16:]))

#a = AESCrypto('this is my key')
#e = a.encrypt('test test')
#print(e)
#print(a.decrypt(e))

def auth_token_generator(user_id, char_names):
    return AESCrypto(g.CFG['crypto_key']).encrypt(user_id + '|'.join(char_names))

def auth_token_validator(auth_token, char_name):
    aes_crypto = AESCrypto(g.CFG['crypto_key'])

    try:
        decrypted = aes_crypto.decrypt(auth_token)
        if char_name in decrypted:
            return True

    finally:
        pass

    return False



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
        while len(self.key) < 32:
            self.key += key

        self.key = self.key[:32]

    def pad(self, str_):
        padding = self.block_size - (len(str_.encode('utf-8')) % self.block_size)
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
        return self.unpad(aes.decrypt(decoded[16:])).decode('utf-8')

#a = AESCrypto('this is my key')
#e = a.encrypt('test 한글 test')
#print(e)
#print(a.decrypt(e))

def generate_auth_token(user_id, char_names):
    char_names_joined = ''
    if len(char_names) > 0:
        char_names_joined = '|'.join(char_names)

    return AESCrypto(g.CFG['crypto_key']).encrypt(user_id + '|' + char_names_joined)

def get_user_id(auth_token):
    aes_crypto = AESCrypto(g.CFG['crypto_key'])

    try:
        char_names = aes_crypto.decrypt(auth_token).split('|')
        user_id = char_names.pop(0)

        return user_id

    finally:
        pass

    return None

def validate_char_name(auth_token, char_name):
    aes_crypto = AESCrypto(g.CFG['crypto_key'])

    try:
        char_names = aes_crypto.decrypt(auth_token).split('|')
        char_names.pop(0)

        if char_name in char_names:
            return True

    finally:
        pass

    return False


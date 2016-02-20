
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
import base64

class AESCrypto:
	def __init__(self, key):
		self.block_size = 32
		self.key = hashlib.sha256(key.encode()).digest()

	def pad(self, str_):
		return str_ + (self.block_size - len(str_) % self.block_size) * chr(self.block_size - len(str_) % self.block_size)

	def unpad(self, str_):
		return str_[:-ord(str_[len(str_) - 1:])]

	def encrypt(self, plain):
		plain = self.pad(plain)
		iv = Random.new().read(AES.block_size)
		aes = AES.new(self.key, AES.MODE_CBC, iv)
		return base64.b64encode(iv + aes.encrypt(plain))

	def decrypt(self, encoded):
		decoded = base64.b64decode(encoded)
		iv = decoded[:16]
		aes = AES.new(self.key, AES.MODE_CBC, iv)
		return self.unpad(aes.decrypt(decoded[16:]))


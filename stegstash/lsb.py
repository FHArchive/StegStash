""" common lsb functions """
from random import SystemRandom
from stegstash.utils import toBin, toFile, getMap, otp

class LSB:
	"""Perform lsb encoding and decoding on an array
	"""
	def __init__(self, array, pointer=0, data=None):
		self.array = array
		self.arrayLen = len(array)
		self.pointer = pointer
		self.data = toBin(data)

	def setLsb(self, bit):
		""" set lsb """
		if self.pointer >= self.arrayLen:
			return
		self.array[self.pointer] = (self.array[self.pointer] & (2**16 - 2)) + bit
		self.pointer += 1


	def getLsb(self):
		""" get lsb """
		if self.pointer >= self.arrayLen:
			return 0
		bit = self.array[self.pointer] & 1
		self.pointer += 1
		return bit


	def setLsb8(self, byte):
		""" set lsb8 """
		for shift in range(8):
			self.setLsb(byte >> shift & 1) # Little endian


	def getLsb8(self):
		""" get lsb8 """
		byte = 0
		for shift in range(8):
			byte += self.getLsb() << shift # Little endian
		return byte, byte == 0


	def setLsb8C(self, char):
		""" set lsb8 char"""
		return self.setLsb8(ord(char))


	def getLsb8C(self):
		""" get lsb8 char """
		byte, nullByte = self.getLsb8()
		return chr(byte), nullByte


	def simpleDecode(self, zeroTerm=True, file=None):
		""" decode a flat array with no encryption

		Args:
		zeroTerm (boolean, optional): stop decoding on \x00 (NUL). Defaults to True.
		file (<file>, optional): file pointer. Defaults to None.
		"""
		data = []
		for _char in range(self.arrayLen // 8):
			char, zero = self.getLsb8()
			if zero and zeroTerm:
				result = bytes(data)
				break
			data.append(char)
		result = bytes(data)
		return toFile(result, file) if file else result


	def simpleEncode(self):
		""" encode a flat array with no encryption """
		for char in self.data:
			if self.pointer >= self.arrayLen - 8:
				break
			self.setLsb8(char)
		self.setLsb8(0) # Null terminate the string
		return self.array


	def decode(self, mapSeed, password="", zeroTerm=True, file=None):
		"""decode data from an array using lsb steganography

		Args:
		mapSeed (string): seed to generate the lsb map
		password (str, optional): password to encrypt the data with. Defaults to "".
		zeroTerm (boolean, optional): stop decoding on \x00 (NUL). Defaults to True.
		file (<file>, optional): file pointer. Defaults to None.

		Returns:
		bytes: data from the image
		"""
		lsbMap = getMap(self.array, mapSeed)
		data = []
		while self.pointer in range(self.arrayLen):
			byte = 0
			shift = 0
			while shift < 8:
				if lsbMap[self.pointer] > 0:
					bit = self.getLsb() # Little endian
					byte += bit << shift
					shift += 1
				else:
					self.pointer += 1 # Increment pointer anyway
			if byte == 0 and zeroTerm:
				result = otp(bytes(data), password, False)
				break
			data.append(byte)
		result = otp(bytes(data), password, False)
		return toFile(result, file) if file else result

	def encode(self, mapSeed, password=""):
		"""encode an array with data using lsb steganography

		Args:
		mapSeed (string): seed to generate the lsb map
		password (str, optional): password to encrypt the data with. Defaults to "".
		"""
		data = otp(self.data, password) + b"\x00"
		lsbMap = getMap(self.array, mapSeed)
		systemRandom = SystemRandom()
		for char in data:
			shift = 0
			while shift < 8:
				if lsbMap[self.pointer] > 0:
					self.setLsb(char >> shift & 1)
					shift += 1
				else:
					self.setLsb(systemRandom.randint(0, 1))
		return self.array

""" common lsb functions """
from random import SystemRandom
import numpy as np
from stegstash.utils import toBin, toFile
from stegstash.simplecrypt import otp

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


	def getMap(self, seed):
		""" get an array map from a seed using python's predictable number generator,
		Isn't security wonderful
		"""
		np.random.seed([ord(char) for char in seed])
		return np.random.randint(0, 2, len(self.array), int)



	def decodeSimpleFlatArr(self, zeroTerm=True, file=None):
		""" decode a flat array with no encryption """
		chars = []
		for _char in range(self.arrayLen // 8):
			char, zero = self.getLsb8()
			if zero and zeroTerm:
				result = bytes(chars)
				break
			chars.append(char)
		result = bytes(chars)
		return toFile(result, file) if file else result


	def encodeSimpleFlatArr(self):
		""" encode a flat array with no encryption """
		for char in self.data:
			if self.pointer >= self.arrayLen - 8:
				break
			self.setLsb8(char)
		self.setLsb8(0) # Null terminate the string
		return self.array


	def decode(self, mapSeed, password, zeroTerm=True, file=None):
		""" decode a data array with a mapSeed and a password """
		lsbMap = self.getMap(mapSeed)
		chars = []
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
				result = otp(bytes(chars), password, False)
				break
			chars.append(byte)
		result = otp(bytes(chars), password, False)
		return toFile(result, file) if file else result

	def encode(self, mapSeed, password):
		""" encode a data array with a mapSeed and a password """
		chars = otp(self.data, password) + b"\x00"
		lsbMap = self.getMap(mapSeed)
		systemRandom = SystemRandom()
		for char in chars:
			shift = 0
			while shift < 8:
				if lsbMap[self.pointer] > 0:
					self.setLsb(char >> shift & 1)
					shift += 1
				else:
					self.setLsb(systemRandom.randint(0, 1))
		return self.array

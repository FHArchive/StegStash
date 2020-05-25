""" utility functions """
from io import BufferedReader, TextIOBase
import numpy as np


def charsToBin(chars):
	""" convert a sequence of chars to binary """
	return chars.encode("utf-8", "backslashreplace")


def binToChars(data):
	""" convert binary to a sequence of chars """
	return data.decode("utf-8", "backslashreplace")


def toBin(data):
	""" convert one of chars| bin| file to bin """
	if isinstance(data, bytes):
		return data
	if isinstance(data, BufferedReader):
		binary = data.read()
		data.close()
		return binary
	if isinstance(data, TextIOBase):
		binary = charsToBin(data.read())
		data.close()
		return binary
	if isinstance(data, str):
		return charsToBin(data)
	return b""


def toChars(data):
	""" convert one of chars| bin| file to chars """
	return binToChars(toBin(data))


def toFile(data, file):
	""" convert one of chars| bin| file to file """
	file.write(toBin(data))
	file.close()

def getMap(array, seed):
	""" get an array map from a seed using python's predictable number generator,
	Isn't security wonderful
	"""
	np.random.seed([ord(char) for char in seed])
	return np.random.randint(0, 2, len(array), int)

def otp(data, password, encodeFlag=True):
	""" do one time pad encoding on a sequence of chars """
	pwLen = len(password)
	if pwLen < 1:
		return data
	out = []
	for index, char in enumerate(data):
		pwPart = ord(password[index % pwLen])
		newChar = char + pwPart if encodeFlag else char - pwPart
		newChar = newChar + 256 if newChar < 0 else newChar
		newChar = newChar - 256 if newChar >= 256 else newChar
		out.append(newChar)
	return bytes(out)

def otpChars(data, password, encodeFlag=True):
	""" do one time pad encoding on a sequence of chars """
	pwLen = len(password)
	if pwLen < 1:
		return data
	out = []
	for index, char in enumerate(data):
		pwPart = ord(password[index % pwLen])
		newChar = ord(char) + pwPart if encodeFlag else ord(char) - pwPart
		newChar = newChar + 128 if newChar < 0 else newChar
		newChar = newChar - 128 if newChar >= 128 else newChar
		out.append(chr(newChar))
	return "".join(out)

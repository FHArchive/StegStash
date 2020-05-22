""" utility functions """
from io import BufferedReader, TextIOBase


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

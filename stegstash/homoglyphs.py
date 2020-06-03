""" encode a text file using homoglyphs """
from random import SystemRandom
import homoglyphs as hg
from stegstash.utils import otp, getMap, toFile, toBin

HOMOGLYPHS = hg.Homoglyphs(categories=('LATIN', 'COMMON', 'CYRILLIC'))


def simpleEncode(openPath, writePath, data):
	"""encode a text file with data using homoglyphs

	Args:
		openPath (string): path to the original text file to open
		writePath (string): path to write the stego-text file
		data (string|bytes|<file>): data to encode
	"""
	with open(openPath, encoding="utf-8") as openData:
		fileData = openData.read()
	position = 0
	output = []
	data = toBin(data)
	for char in data + b"\x00":
		shift = 0
		while shift < 8:
			result, shift = encodeGlyph(fileData, position, char, shift)
			output.append(result)
			position += 1
	output.append(fileData[position:])
	with open(writePath, "w", encoding="utf-8") as writeData:
		writeData.write("".join(output))


def simpleDecode(openPath, zeroTerm=True, file=None):
	"""decode data from an text file using homoglyphs

	Args:
		openPath (string): path to the stego-text file to decode
		zeroTerm (boolean, optional): stop decoding on \x00 (NUL). Defaults to True.
		file (<file>, optional): file pointer. Defaults to None.

	Returns:
		bytes: data from the text file
	"""
	with open(openPath, encoding="utf-8") as openData:
		fileData = openData.read()
	position = 0
	data = []
	for _char in fileData:
		byte = 0
		shift = 0
		while shift < 8:
			byte, shift = decodeGlyph(fileData, position, byte, shift)
			position += 1
		if byte == 0 and zeroTerm:
			break
		data.append(byte)
	result = bytes(data)
	return toFile(result, file) if file else result



def encode(openPath, writePath, data, mapSeed, password=""):
	"""encode a text file with data using homoglyphs

	Args:
		openPath (string): path to the original text file to open
		writePath (string): path to write the stego-text file
		data (string): data to encode
		mapSeed (string): seed to generate the lsb map
		password (str, optional): password to encrypt the data with. Defaults to "".
	"""
	with open(openPath, encoding="utf-8") as openData:
		fileData = openData.read()
	position = 0
	output = []
	data = otp(toBin(data), password) + b"\x00"
	encodeMap = getMap(fileData, mapSeed)
	systemRandom = SystemRandom()
	for char in data:
		shift = 0
		while shift < 8:
			if encodeMap[position] > 0:
				result, shift = encodeGlyph(fileData, position, char, shift)
			else:
				result, _shift = encodeGlyph(fileData, position,
				systemRandom.randint(0, 1) << shift, shift)
			output.append(result)
			position += 1
	output.append(fileData[position:])
	with open(writePath, "w", encoding="utf-8") as writeData:
		writeData.write("".join(output))


def decode(openPath, mapSeed, password="", zeroTerm=True, file=None):
	"""decode data from an text file using homoglyphs

	Args:
		openPath (string): path to the stego-text file to decode
		mapSeed (string): seed to generate the lsb map
		password (str, optional): password to encrypt the data with. Defaults to "".
		zeroTerm (boolean, optional): stop decoding on \x00 (NUL). Defaults to True.
		file (<file>, optional): file pointer. Defaults to None.

	Returns:
		bytes: data from the text file
	"""
	with open(openPath, encoding="utf-8") as openData:
		fileData = openData.read()
	position = 0
	data = []
	decodeMap = getMap(fileData, mapSeed)
	for _char in fileData:
		byte = 0
		shift = 0
		while shift < 8:
			if decodeMap[position] > 0:
				byte, shift = decodeGlyph(fileData, position, byte, shift)
			position += 1
		if byte == 0 and zeroTerm:
			break
		data.append(byte)
	result = otp(bytes(data), password, False)
	return toFile(result, file) if file else result


def encodeGlyph(fileData, position, byte, shift):
	""" encode a single glyph (1/8th of hidden data)"""
	combinations = HOMOGLYPHS.get_combinations(fileData[position])
	if fileData[position] not in (" ", "\t", "\n") and len(combinations) > 1:
		return combinations[byte >> shift & 1], shift + 1
	return combinations[0], shift


def decodeGlyph(fileData, position, byte, shift):
	""" decode a single glyph (1/8th of hidden data)"""
	combinations = HOMOGLYPHS.get_combinations(fileData[position])
	if fileData[position] not in (" ", "\t", "\n") and len(combinations) > 1:
		return byte + (
		(0 if combinations[0] == fileData[position] else 1) << shift), shift + 1
	return byte, shift


def detectSteg(openPath):
	"""Detect the use of homoglyph stegonography.

	False positives can be easily triggered (this checks for non ascii chars)

	Args:
		openPath (string): path to the text file to analyse

	Returns:
		boolean: True if this lib has been used to hide data
	"""
	try:
		open(openPath, encoding="ascii").read()
		return False
	except UnicodeDecodeError:
		return True

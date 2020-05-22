""" encode a text file using homoglyphs """

import homoglyphs as hg

HOMOGLYPHS = hg.Homoglyphs(categories=('LATIN', 'COMMON', 'CYRILLIC'))

def simpleEncode(openPath, writePath, chars):
	""" encode """
	with open(openPath, encoding="utf-8") as openData:
		data = openData.read()
	data = encodeData(data, chars)
	with open(writePath, "w", encoding="utf-8") as writeData:
		writeData.write(data)


def simpleDecode(openPath, zeroTerm=True):
	""" decode """
	with open(openPath, encoding="utf-8") as openData:
		data = openData.read()
	return decodeData(data, zeroTerm)



def encodeData(data, chars):
	""" encode data with chars """
	position = 0
	output = []
	for char in chars:
		shift = 0
		while shift < 8:
			result, shift = encodeGlyph(data, position, char, shift)
			output.append(result)
			position += 1
	shift = 0
	while shift < 8:
		result, shift = encodeGlyph(data, position, chr(0), shift)
		output.append(result)
		position += 1
	output.append(data[position:])
	return "".join(output)

def decodeData(data, zeroTerm=True):
	""" decode homoglyph data """
	position = 0
	chars = []
	for _char in data:
		byte = 0
		shift = 0
		while shift < 8:
			byte, shift = decodeGlyph(data, position, byte, shift)
			position += 1
		if byte == 0 and zeroTerm:
			return "".join(chars)
		chars.append(chr(byte))
	return "".join(chars)


def encodeGlyph(data, position, char, shift):
	""" encode a single glyph (1/8th of hidden data)"""
	combinations = HOMOGLYPHS.get_combinations(data[position])
	if data[position] not in (" ", "\t", "\n") and len(combinations) > 1:
		return combinations[ord(char) >> shift & 1], shift + 1
	return combinations[0], shift


def decodeGlyph(data, position, byte, shift):
	""" decode a single glyph (1/8th of hidden data)"""
	combinations = HOMOGLYPHS.get_combinations(data[position])
	if data[position] not in (" ", "\t", "\n") and len(combinations) > 1:
		return byte + ((0 if combinations[0] == data[position] else 1) << shift), shift + 1
	return byte, shift

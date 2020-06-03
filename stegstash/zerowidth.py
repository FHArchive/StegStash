""" Uses zero width chars to hide data

One similar project uses the following code points:
Unicode u200b to u200f
zero width space
zero width non joiner
zero width joiner
left to right mark
right to left mark

These are invisible in VSCode, Notepad.exe and PythonIDLE

See the table below for a comparison of various glyphs in a series of popular text
editors

|Char Code|   Char Name|Notepad.exe|VSCode|PythonIDLE|KWrite|EMACS|<safe>|MsWord|    Utf8|
|---------|------------|-----------|------|----------|------|-----|------|------|--------|
|<control>|   <control>|          x|     x|         x|     x|    x|     x|     x|        |
|u00ad    |  SoffHyphen|          x|     +|         x|     x|    x|     x|     x|        |
|u034f    |   CombiningGraphemeJoiner|+| +|         +|     +|    x|     x|     +|        |
|u200b    |     ZWSpace|          +|     +|         +|     +|    +|     +|     +|E2 80 8B|
|u200c    | ZWNonJoiner|          +|     +|         +|     +|    +|     +|     +|E2 80 8C|
|u200d    |    ZWJoiner|          +|     +|         +|     +|    +|     +|     +|E2 80 8D|
|u200e    |     LTRMark|          +|     +|         +|     +|    +|     +|     +|E2 80 8E|
|u200f    |     RTLMark|          +|     +|         +|     +|    +|     +|     +|E2 80 8F|
|u202a    |LTREmbedding|          +|     +|         +|     +|    +|     +|     +|E2 80 AA|
|u202b    |RTLEmbedding|          +|     +|         +|     +|    +|     +|     +|        |
|u202c    |  PopDirectionalFormatting|+| +|         +|     +|    +|     +|     +|E2 80 AC|
|u202d    | LTROverride|          +|     +|         +|     +|    +|     +|     +|E2 80 AD|
|u202e    | RTLOverride|          x|     x|         +|     x|    x|     x|     x|        |
|u2060    |  WordJoiner|          x|     +|         +|     +|    +|     x|     +|        |
|u2061    |   FunctionApplication|+|     +|         +|     +|    +|     +|     x|E2 81 A1|
|u2062    |        InvisibleTimes|+|     +|         +|     +|    +|     +|     x|E2 81 A2|
|u2063    |    InvisibleSeperator|+|     +|         +|     +|    +|     +|     x|E2 81 A3|
|u2064    |InvisiblePlue|         +|     +|         +|     +|    +|     +|     x|E2 81 A4|
|u2065    |   <unknown>|          x|     +|         x|     +|    x|     x|     x|        |
|u2066    |  LTRIsolate|          x|     +|         x|     +|    +|     x|     x|        |
|u2067    |  RTLIsolate|          x|     +|         x|     +|    +|     x|     x|        |
|u2068    |    FirstStrongIsolate|x|     +|         x|     +|    +|     x|     x|        |
|u2069    | PopDirectionalIsolate|x|     +|         x|     +|    +|     x|     x|        |
|u206a    |  InhibitSymmetricSwapping|+| +|         +|     +|    +|     +|     x|E2 81 AA|
|u206b    | ActivateSymmetricSwapping|+| +|         +|     +|    +|     +|     x|E2 81 AB|
|u206c    | InhibitArabicFormSwapping|+| +|         +|     +|    +|     +|     x|E2 81 AC|
|u206d    |ActivateArabicFormSwapping|+| +|         +|     +|    +|     +|     x|E2 81 AD|
|u206e    |   NationalDigitShapes|+|     +|         +|     +|    +|     +|     x|E2 81 AE|
|u206f    |    NominalDigitShapes|+|     +|         +|     +|    +|     +|     x|E2 81 AF|
|u2068    |    FirstStrongIsolate|x|     +|         x|     +|    +|     x|     x|        |

The likes of vim/gvim show these up but a typical user is unlikely to be using
those text editors.

Though not a text editor, Microsoft Word seems pretty good at higlighting some
of these chars (at least better than initially expected). There is a possibility
that a user may have configured word to open a text file (though not completely
likely). To mitigate this slim risk a safe mode will be added to disable use of
these chars
"""
from stegstash.utils import otp, getMap, toFile, toBin

HIDDEN_SAFE = [
b"\xe2\x80\x8b", b"\xe2\x80\x8c", b"\xe2\x80\x8d", b"\xe2\x80\x8e",
b"\xe2\x80\x8f", b"\xe2\x80\xaa", b"\xe2\x80\xac", b"\xe2\x80\xad"] # 3 swc

HIDDEN = HIDDEN_SAFE + [
b"\xe2\x81\xa1", b"\xe2\x81\xa2", b"\xe2\x81\xa3", b"\xe2\x81\xa4",
b"\xe2\x81\xaa", b"\xe2\x81\xab", b"\xe2\x81\xac", b"\xe2\x81\xad",
b"\xe2\x81\xae", b"\xe2\x81\xaf"] # 2 swc


def encode(openPath, writePath, data, mapSeed, password="", safe=True):
	"""encode a text file with data using zero width chars

	Args:
		openPath (string): path to the original text file to open
		writePath (string): path to write the stego-text file
		data (string|bytes|<file>): data to encode
		mapSeed (string): seed to generate the lsb map
		password (str, optional): password to encrypt the data with. Defaults to "".
		safe (boolean, optional): use a reduced set of chars to show in fewer
		editors. Defaults to True.
	"""
	with open(openPath, "rb") as openData:
		fileData = openData.read()
	position = 0
	pointer = 0
	zwcMap = getMap(fileData, mapSeed)
	encodeData = otp(toBin(data), password) + b"\x00"
	while pointer < len(encodeData):
		if zwcMap[position] > 0:
			position, fileData = encodeCharZero(fileData, position, encodeData[pointer], safe)
			pointer += 1
		else:
			position += getUtf8Size(fileData, position)[0] # increment by char size
	with open(writePath, "wb") as writeData:
		writeData.write(fileData)


def decode(openPath, mapSeed, password="", zeroTerm=True, file=None, safe=True):
	"""decode data from a text file using zero width chars

	Args:
		openPath (string): path to the stego-text file to decode
		mapSeed (string): seed to generate the lsb map
		password (str, optional): password to encrypt the data with. Defaults to "".
		zeroTerm (boolean, optional): stop decoding on \x00 (NUL). Defaults to True.
		file (<file>, optional): file pointer. Defaults to None.
		safe (boolean, optional): use a reduced set of chars to show in fewer
		editors. Defaults to True.

	Returns:
		bytes: data from the text file
	"""
	with open(openPath, "rb") as openData:
		fileData = openData.read()
	position = 0
	data = []
	zwcMap = getMap(fileData, mapSeed)
	for _char in fileData:
		if zwcMap[position] > 0:
			position, byte = decodeCharZero(fileData, position, safe)
			if byte == 0 and zeroTerm:
				break
			data.append(byte)
		else:
			position += getUtf8Size(fileData, position)[0] # increment by char size
	result = otp(bytes(data), password, False)
	return toFile(result, file) if file else result


def simpleEncode(openPath, writePath, data, safe=True):
	"""encode a text file with data using zero width chars

	Args:
		openPath (string): path to the original text file to open
		writePath (string): path to write the stego-text file
		data (string|bytes|<file>): data to encode
		safe (boolean, optional): use a reduced set of chars to show in fewer
		editors. Defaults to True.
	"""
	with open(openPath, "rb") as openData:
		fileData = openData.read()
	position = 0
	for char in toBin(data) + b"\x00":
		position, fileData = encodeCharZero(fileData, position, char, safe)
	with open(writePath, "wb") as writeData:
		writeData.write(fileData)


def simpleDecode(openPath, zeroTerm=True, file=None, safe=True):
	"""decode data from a text file using zero width chars

	Args:
		openPath (string): path to the stego-text file to decode
		zeroTerm (boolean, optional): stop decoding on \x00 (NUL). Defaults to True.
		file (<file>, optional): file pointer. Defaults to None.
		safe (boolean, optional): use a reduced set of chars to show in fewer
		editors. Defaults to True.

	Returns:
		bytes: data from the text file
	"""
	with open(openPath, "rb") as openData:
		fileData = openData.read()
	position = 0
	data = []
	for _char in fileData:
		position, byte = decodeCharZero(fileData, position, safe)
		if byte == 0 and zeroTerm:
			break
		data.append(byte)
	result = bytes(data)
	return toFile(result, file) if file else result


def encodeCharZero(fileData, pointer, char, safe=True):
	""" encode a char as a series of zero width chars such that the result looks
	like foobar -> f\0o\0o\0bar
	"""
	charMap = HIDDEN_SAFE if safe else HIDDEN
	base = len(charMap)
	for exponent in range(2, -1, -1):
		value = char // base**exponent
		pointer, fileData = writeUtf8(pointer, charMap[value], fileData)
		char -= base**exponent * value
	return pointer, fileData


def decodeCharZero(fileData, pointer, safe=True):
	""" decode a series of zero width chars as a char such that \0 is read
	from f\0o\0o\0bar
	"""
	charMap = HIDDEN_SAFE if safe else HIDDEN
	base = len(charMap)
	value = 0
	for exponent in range(2, -1, -1):
		pointer, char = readUtf8(pointer, fileData)
		value += charMap.index(char) * base**exponent
	return pointer, value


def writeUtf8(pointer, newBytes, byteStream):
	""" write a series of utf8 bytes after an existing char and advance the
	pointer
	"""
	size, pointer = getUtf8Size(byteStream, pointer)
	pointer += size
	return pointer + len(newBytes), byteStream[:pointer] + newBytes + byteStream[pointer:]


def readUtf8(pointer, byteStream):
	""" read the next zero char and advance the pointer
	1 utf8: 0
	2 utf8: 110
	3 utf8: 1110
	4 utf8: 11110
	"""
	size, pointer = getUtf8Size(byteStream, pointer)
	pointer += size # point to the zero char
	size, pointer = getUtf8Size(byteStream, pointer)
	return pointer + size, byteStream[pointer:pointer + size]


def getUtf8Size(byteStream, pointer):
	""" get the size of the next utf8 char """
	byte = byteStream[pointer]
	if byte < 128:
		return 1, pointer
	if byte & 0b11110000 == 0b11110000:
		return 4, pointer
	if byte & 0b11100000 == 0b11100000:
		return 3, pointer
	if byte & 0b11000000 == 0b11000000:
		return 2, pointer
	if byte & 0b10000000 == 0b10000000:
		return getUtf8Size(byteStream, pointer - 1) # backtrack as we are reading
		# in the middle of a stream
	return -1, -1 # error state


def detectSteg(openPath):
	""" detect the use of zero width char steganography

	Args:
		openPath (string): path to the text file to analyse

	Returns:
		boolean: True if this lib has been used to hide data
	"""
	with open(openPath, "rb") as openData:
		fileData = openData.read()
	if any(zwc in fileData for zwc in HIDDEN):
		return True
	return False

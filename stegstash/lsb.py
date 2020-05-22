""" common lsb functions """


def setLsb(array, pointer, bit):
	""" set lsb """
	if pointer >= len(array):
		return pointer
	array[pointer] = (array[pointer] & (2**16 - 2)) + bit
	return pointer + 1


def getLsb(array, pointer):
	""" get lsb """
	if pointer >= len(array):
		return pointer, 0
	return pointer + 1, array[pointer] & 1


def setLsb8(array, pointer, byte):
	""" set lsb8 """
	for shift in range(8):
		pointer = setLsb(array, pointer, byte >> shift & 1) # Little endian
	return pointer


def getLsb8(array, pointer):
	""" get lsb8 """
	byte = 0
	for shift in range(8):
		pointer, bit = getLsb(array, pointer) # Little endian
		byte += bit << shift
	return pointer, byte, byte == 0


def setLsb8C(array, pointer, char):
	""" set lsb8 char"""
	return setLsb8(array, pointer, ord(char))


def getLsb8C(array, pointer):
	""" get lsb8 char """
	pointer, byte, nullByte = getLsb8(array, pointer)
	return pointer, chr(byte), nullByte


def decodeSimpleFlatArr(array, zeroTerm=True):
	""" decode a flat array with no encryption """
	pointer = 0
	chars = []
	for _char in range(len(array) // 8):
		pointer, char, zero = getLsb8C(array, pointer)
		if zero and zeroTerm:
			return "".join(chars)
		chars.append(char)
	return "".join(chars)


def encodeSimpleFlatArr(array, chars):
	""" encode a flat array with no encryption """
	pointer = 0
	for char in chars:
		pointer = setLsb8C(array, pointer, char)
	pointer = setLsb8(array, pointer, 0) # Null terminate the string
	return array

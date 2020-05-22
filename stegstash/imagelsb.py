""" encode and decode methods """
from random import SystemRandom
import numpy as np
from PIL import Image
from metprint import LogType, Logger, FHFormatter
from stegstash.lsb import setLsb, getLsb, decodeSimpleFlatArr, encodeSimpleFlatArr
from stegstash.simplecrypt import otp

exts = ["bmp", "gif", "png", "webp"]


def extNotLossless(fileName):
	""" Output the file extension not lossless error """
	Logger(FHFormatter()).logPrint(
	"File extension is not lossless: " + fileName + "! Must be " + "one of \"" +
	", \"".join(exts) + "\"", LogType.ERROR)


def encode(openPath, writePath, chars, imageMapSeed, password=""):
	""" encode an image with lsb data """
	image, size = openImg(openPath)
	pointer = 0
	chars = otp(chars, password)
	imgMap = getImgMap(imageMapSeed, image)
	systemRandom = SystemRandom()
	for char in chars:
		shift = 0
		while shift < 8:
			if imgMap[pointer] > 0:
				pointer = setLsb(image, pointer, ord(char) >> shift & 1)
				shift += 1
			else:
				pointer = setLsb(image, pointer, systemRandom.randint(0, 1))
	writeImg(writePath, image, size)


def decode(openPath, imageMapSeed, password="", zeroTerm=True):
	""" decode an image and return a byte string """
	image, _size = openImg(openPath)
	pointer = 0
	imgMap = getImgMap(imageMapSeed, image)
	chars = []
	while pointer in range(len(image)):
		byte = 0
		shift = 0
		while shift < 8:
			if imgMap[pointer] > 0:
				_pointer, bit = getLsb(image, pointer) # Little endian
				byte += bit << shift
				shift += 1
			pointer += 1
		if byte == 0 and zeroTerm:
			return otp("".join(chars), password, False)
		chars.append(chr(byte))
	return otp("".join(chars), password, False)


def simpleEncode(openPath, writePath, chars):
	""" encode an image with lsb data """
	image, size = openImg(openPath)
	image = encodeSimpleFlatArr(image, chars)
	writeImg(writePath, image, size)


def simpleDecode(openPath, zeroTerm=True):
	""" decode an image and return a byte string """
	image, _size = openImg(openPath)
	return decodeSimpleFlatArr(image, zeroTerm)


def getImgMap(seed, image):
	""" get an image map from a seed using python's predictable number generator,
	Isn't security wonderful
	"""
	np.random.seed([ord(char) for char in seed])
	return np.random.randint(0, 2, len(image), int)


def openImg(path):
	""" open an image as numpy array """
	# Lossless BMP, GIF, PNG, WEBP (some)
	fileExt = path.split(".")[-1].lower()
	if fileExt not in exts:
		extNotLossless(path)
		raise ValueError
	image = Image.open(path)
	return np.array(image.convert("RGBA")).flatten(), image.size


def writeImg(path, image, imageSize):
	""" write a numpy array to a path """
	fileExt = path.split(".")[-1].lower()
	if fileExt not in exts:
		extNotLossless(path)
		raise ValueError
	Image.fromarray(image.reshape(imageSize[1], imageSize[0], 4)).save(path)

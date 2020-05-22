""" encode and decode methods """
import numpy as np
from PIL import Image
from metprint import LogType, Logger, FHFormatter
from stegstash.lsb import LSB

exts = ["bmp", "gif", "png", "webp"]


def extNotLossless(fileName):
	""" Output the file extension not lossless error """
	Logger(FHFormatter()).logPrint(
	"File extension is not lossless: " + fileName + "! Must be " + "one of \"" +
	", \"".join(exts) + "\"", LogType.ERROR)


def encode(openPath, writePath, chars, imageMapSeed, password=""):
	""" encode an image with lsb data """
	image, size = openImg(openPath)
	encodeLsb = LSB(image, data=chars)
	encodeLsb.encode(imageMapSeed, password)
	writeImg(writePath, image, size)


def decode(openPath, imageMapSeed, password="", zeroTerm=True, file=None):
	""" decode an image and return a byte string """
	image, _size = openImg(openPath)
	decodeLsb = LSB(image)
	return decodeLsb.decode(imageMapSeed, password, zeroTerm, file)


def simpleEncode(openPath, writePath, chars):
	""" encode an image with lsb data """
	image, size = openImg(openPath)
	encodeLsb = LSB(image, data=chars)
	image = encodeLsb.encodeSimpleFlatArr()
	writeImg(writePath, image, size)


def simpleDecode(openPath, zeroTerm=True, file=None):
	""" decode an image and return a byte string """
	image, _size = openImg(openPath)
	decodeLsb = LSB(image)
	return decodeLsb.decodeSimpleFlatArr(zeroTerm, file)


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

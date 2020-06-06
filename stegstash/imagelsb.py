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


def encode(openPath, writePath, data, imageMapSeed, password=""):
	"""encode an image with data using lsb steganography

	Args:
		openPath (string): path to the original image to open
		writePath (string): path to write the stego-image
		data (string|bytes|<file>): data to encode
		imageMapSeed (string): seed to generate the lsb map
		password (str, optional): password to encrypt the data with. Defaults to "".
	"""
	image, size, mode = openImg(openPath)
	encodeLsb = LSB(image, data=data)
	encodeLsb.encode(imageMapSeed, password)
	writeImg(writePath, image, size, mode)


def decode(openPath, imageMapSeed, password="", zeroTerm=True, file=None):
	"""decode data from an image using lsb steganography

	Args:
		openPath (string): path to the stego-image to decode
		imageMapSeed (string): seed to generate the lsb map
		password (str, optional): password to encrypt the data with. Defaults to "".
		zeroTerm (boolean, optional): stop decoding on \x00 (NUL). Defaults to True.
		file (<file>, optional): file pointer. Defaults to None.

	Returns:
		bytes: data from the image
	"""
	image, _size, _mode = openImg(openPath)
	decodeLsb = LSB(image)
	return decodeLsb.decode(imageMapSeed, password, zeroTerm, file)


def simpleEncode(openPath, writePath, data):
	"""encode an image with data using lsb steganography

	Args:
		openPath (string): path to the original image to open
		writePath (string): path to write the stego-image
		data (string|bytes|<file>): data to encode
	"""
	image, size, mode = openImg(openPath)
	encodeLsb = LSB(image, data=data)
	image = encodeLsb.simpleEncode()
	writeImg(writePath, image, size, mode)


def simpleDecode(openPath, zeroTerm=True, file=None):
	"""decode data from an image using lsb steganography

	Args:
		openPath (string): path to the stego-image to decode
		zeroTerm (boolean, optional): stop decoding on \x00 (NUL). Defaults to True.
		file (<file>, optional): file pointer. Defaults to None.

	Returns:
		bytes: data from the image
	"""
	image, _size, _mode = openImg(openPath)
	decodeLsb = LSB(image)
	return decodeLsb.simpleDecode(zeroTerm, file)


def openImg(path):
	"""Open an image as a numpy array

	Args:
		path (string): path to the image to open

	Returns:
		numpy.array, (int, int), string: A 1D numpy array containing image
		pixels, image size, image mode
	"""
	# Lossless BMP, GIF, PNG, WEBP (some)
	fileExt = path.split(".")[-1].lower()
	if fileExt not in exts:
		extNotLossless(path)
		raise ValueError
	image = Image.open(path)
	mode = image.mode
	return np.array(image.convert("RGBA" if mode in ("RGBA",
	"PA") else "RGB")).flatten(), image.size, mode


def writeImg(path, image, imageSize, mode):
	"""Write a 1D numpy array to a file

	Args:
		path (string): path to the image to save
		image (numpy.array): 1D numpy array containing image pixels
		imageSize ((int, int)): size of the image
		mode (string): PIL Image mode typically one of "RGBA", "RGB", "PA", "P"
	"""
	fileExt = path.split(".")[-1].lower()
	if fileExt not in exts:
		extNotLossless(path)
		raise ValueError
	Image.fromarray(image.reshape(imageSize[1], imageSize[0],
	4 if mode in ("RGBA", "PA") else 3)).convert(mode).save(path)

def visual(openPath, imgPath):
	"""Visualize the use of lsb stegonography.

	Args:
		openPath (string): path to the text file to analyse
		imgPath (string): image file path
	"""
	image, size, mode = openImg(openPath)
	imageLen = len(image)
	for pointer in range(imageLen):
		image[pointer] = (image[pointer] & 1) * 255
	writeImg(imgPath, image, size, mode)

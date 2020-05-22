""" append data to an image after the end """
'''
readonly jpg_start="ffd8"
readonly jpg_end="ff d9"
readonly png_start="8950 4e47 0d0a 1a0a"
readonly png_end="49 45 4e 44 ae 42 60 82"
readonly gif_start="4749 4638 3961"
readonly gif_end="00 3b"

'''
from metprint import LogType, Logger, FHFormatter
from stegstash.utils import toBin
from stegstash.simplecrypt import otp

endKeys = {
"jpg": b"\xff\xd9", "png": b"\x49\x45\x4e\x44\xae\x42\x60\x82",
"gif": b"\x00\x3b"}


def extNotSupported(fileName):
	""" Output the file extension not supported error """
	exts = ["jpg", "png", "gif"]
	Logger(FHFormatter()).logPrint(
	"File extension is not supported for file: " + fileName + "! Must be " +
	"one of \"" + ", \"".join(exts) + "\"", LogType.ERROR)


def encode(openPath, writePath, chars, password=""):
	""" encode an image with data """
	data, fileExt = openImg(openPath)
	imageWriteData = data[:data.find(endKeys[fileExt]) + len(endKeys[fileExt])]
	writeImg(writePath, imageWriteData + otp(toBin(chars), password))


def decode(openPath, password=""):
	""" decode an image with data """
	data, fileExt = openImg(openPath)
	readData = data[data.find(endKeys[fileExt]) + len(endKeys[fileExt]):]
	return otp(readData, password, False)


def openImg(path):
	""" open an image and get its data """
	fileExt = path.split(".")[-1].lower()
	if fileExt not in endKeys:
		extNotSupported(path)
		raise ValueError
	with open(path, "rb") as imageData:
		data = imageData.read()
	return data, fileExt


def writeImg(path, byteArr):
	""" write to an image """
	fileExt = path.split(".")[-1].lower()
	if fileExt not in endKeys:
		extNotSupported(path)
		raise ValueError
	with open(path, "wb") as imageData:
		imageData.write(byteArr)

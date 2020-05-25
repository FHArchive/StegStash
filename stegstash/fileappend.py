""" append data to an image after the end
# Files and byte(s) terminators

jpg: \xff\xd9
png: \x49\x45\x4e\x44\xae\x42\x60\x82 (IEND.b`. - think only IEND is required)
gif: \x00\x3b (\x3b according to wikipedia)
"""
from metprint import LogType, Logger, FHFormatter
from stegstash.utils import toBin, toFile, otp

endKeys = {
"jpg": b"\xff\xd9", "png": b"\x49\x45\x4e\x44\xae\x42\x60\x82",
"gif": b"\x00\x3b"}


def extNotSupported(fileName):
	""" Output the file extension not supported error """
	exts = ["jpg", "png", "gif"]
	Logger(FHFormatter()).logPrint(
	"File extension is not supported for file: " + fileName + "! Must be " +
	"one of \"" + ", \"".join(exts) + "\"", LogType.ERROR)


def encode(openPath, writePath, appendData, password=""):
	"""encode a file with data by appending binary after the end of the file

	Args:
		openPath (string): path to the original file to open
		writePath (string): path to write the stego-file
		appendData (string|bytes|<file>): data to encode
		password (str, optional): password to encrypt the data with. Defaults to "".
	"""
	data, fileExt = openFile(openPath)
	imageWriteData = data[:data.find(endKeys[fileExt]) + len(endKeys[fileExt])]
	writeFile(writePath, imageWriteData + otp(toBin(appendData), password))


def decode(openPath, password="", file=None):
	"""decode data from a file by extracting data after end of file

	Args:
		openPath (string): path to the stego-file to decode
		password (str, optional): password to encrypt the data with. Defaults to "".
		file (<file>, optional): file pointer. Defaults to None.

	Returns:
		bytes: data from the image
	"""
	""" decode an image with data """
	data, fileExt = openFile(openPath)
	readData = data[data.find(endKeys[fileExt]) + len(endKeys[fileExt]):]
	result = otp(readData, password, False)
	return toFile(result, file) if file else result


def openFile(path):
	"""Open an file to bytes

	Args:
		path (string): path to the file to open

	Returns:
		bytes: file data
	"""
	""" open a file and get its data """
	fileExt = path.split(".")[-1].lower()
	if fileExt not in endKeys:
		extNotSupported(path)
		raise ValueError
	with open(path, "rb") as fileData:
		data = fileData.read()
	return data, fileExt


def writeFile(path, byteArr):
	"""Write bytes to a file

	Args:
		path (string): path to the file to save
		byteArr (bytes): bytes to write to the file
	"""
	fileExt = path.split(".")[-1].lower()
	if fileExt not in endKeys:
		extNotSupported(path)
		raise ValueError
	with open(path, "wb") as fileData:
		fileData.write(byteArr)

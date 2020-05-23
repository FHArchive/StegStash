""" common zip steganography functions """

from zipfile import ZIP_DEFLATED, ZipFile
from shutil import copyfile
from math import ceil
from mutablezip import MutableZipFile
from stegstash.utils import toBin



def encodeComment(openPath, writePath, data):
	"""encode an microsoft office file with data by inserting into xml comments

	Args:
		openPath (string): path to the original office document to open
		writePath (string): path to write the stego-office document
		data (string|bytes|<file>): data to encode
	"""
	# iterate xml files and inject data in chunks
	copyfile(openPath, writePath)
	with MutableZipFile(writePath, "a", compression=ZIP_DEFLATED) as zipFile:
		files = []
		for file in zipFile.namelist():
			if file.endswith((".xml")):
				files.append(file)
		files.sort()
		# Split data into chunks
		chunkLen = ceil(len(data) / len(files))
		data = toBin(data)
		for iteration, file in enumerate(files):
			with zipFile.open(file, "r") as xmlFile:
				lines = [line.strip() for line in xmlFile.readlines()]
			lines.insert(
			1, b"<!--" + data[chunkLen * (iteration):chunkLen * (iteration+1)] + b"-->")
			zipFile.writestr(file, b"\n".join(lines))


def decodeComment(openPath):
	"""decode data from a microsoft office file by reading xml comments

	Args:
		openPath (string): path to the stego-office document to decode

	Returns:
		bytes: data from the image
	"""
	# iterate xml files and fetch comments - sort files alphanumerically
	with ZipFile(openPath, "r", compression=ZIP_DEFLATED) as zipFile:
		files = []
		data = []
		for file in zipFile.namelist():
			if file.endswith((".xml")):
				files.append(file)
		files.sort()
		for file in files:
			with zipFile.open(file, "r") as xmlFile:
				lines = [line.strip() for line in xmlFile.readlines()]
			data.append(lines[1].replace(b"<!--", b"").replace(b"-->", b""))
		return b"".join(data)

""" hide data and files in a docx, pptx etc
Functions:
- Add data as a comment in xml such as [Content_Types].xml
- Add a file and update [Content_Types].xml
Limitations:
- These do not persist modification. i.e. the data will be lost in the event of
a user modifying the document (tested in LibreOffice and Microsoft Word 365:2004)
"""

from zipfile import ZIP_DEFLATED, ZipFile
from shutil import copyfile
from mutablezip import MutableZipFile
from stegstash.utils import toBin, toFile, otp
from stegstash import zipfile


def encodeComment(openPath, writePath, data):
	"""encode an microsoft office file with data by inserting into xml comments

	Args:
		openPath (string): path to the original office document to open
		writePath (string): path to write the stego-office document
		data (string|bytes|<file>): data to encode
	"""
	# iterate xml files and inject data in chunks
	zipfile.encodeComment(openPath, writePath, data)


def decodeComment(openPath):
	"""decode data from a microsoft office file by reading xml comments

	Args:
		openPath (string): path to the stego-office document to decode

	Returns:
		bytes: data from the image
	"""
	# iterate xml files and fetch comments - sort files alphanumerically
	return zipfile.decodeComment(openPath)


def encodeFile(openPath, writePath, file, fileName="application.xml",
password=""):
	""" encode data as a file """
	# Add one of the following:
	# <Override PartName="/docProps/<file>" ContentType="application/octet-stream"/>
	# <Override PartName="/docProps/application.xml"
	# ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
	copyfile(openPath, writePath)
	with MutableZipFile(writePath, "a", compression=ZIP_DEFLATED) as zipFile:
		zipFile.writestr("docProps/" + fileName, otp(toBin(file), password))
		with zipFile.open("[Content_Types].xml", "r") as xmlFile:
			lines = [line.strip() for line in xmlFile.readlines()]
		lines[1] = lines[1].replace(
		b"</Types>", b"<Override PartName=\"/docProps/" + fileName.encode("utf-8") +
		b"\" ContentType=\"application/" +
		(b"vnd.openxmlformats-officedocument.extended-properties+xml"
		if fileName == "application.xml" else b"octet-stream") + b"\"/></Types>")
		zipFile.writestr("[Content_Types].xml", b"\n".join(lines))


def decodeFile(openPath, password="", filePointer=None):
	"""decode data from a microsoft office file by extracting the file

	Args:
		openPath (string): path to the stego-document to decode
		password (str, optional): password to encrypt the data with. Defaults to "".
		filePointer (<file>, optional): pointer to the file. Defaults to None.

	Returns:
		bytes: data from the image
	"""
	# Look for "/docProps/*.[* not .xml]" or "/docProps/application.xml"
	with ZipFile(openPath, "r", compression=ZIP_DEFLATED) as zipFile:
		files = []
		for file in zipFile.namelist():
			if file.startswith("docProps") and (not file.endswith(
			(".xml", ".rels")) or file.endswith("application.xml")):
				files.append(file)
		with zipFile.open(files[0], "r") as dataFile:
			data = otp(dataFile.read(), password, False)
		return toFile(data, filePointer) if filePointer else data


def detectSteg(openPath, checkDocPropsOnly=True):
	""" detect the use of microsoft office steganography

	False positives can be triggered by including media in a document when
	checkDocPropsOnly is set to False

	Args:
		openPath (string): path to the text file to analyse
		checkDocPropsOnly (boolean, optional): look under docProps only to
		mitigate one source of false positives. Defaults to True.

	Returns:
		boolean: True if this lib has been used to hide data
	"""
	with ZipFile(openPath, "r", compression=ZIP_DEFLATED) as zipFile:
		files = []
		for file in zipFile.namelist():
			if (not checkDocPropsOnly or
			file.startswith("docProps")) and (not file.endswith(
			(".xml", ".rels")) or file.endswith("application.xml")):
				files.append(file)
	return len(files) > 0 or zipfile.detectSteg(openPath)

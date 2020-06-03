""" hide data and files in a odt, odp etc
Functions:
- Add data as a comment in xml such as META-INF/manifest.xml
- Add a file and update META-INF/manifest.xml
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
	"""encode an open document file with data by inserting into xml comments

	Args:
		openPath (string): path to the original open document to open
		writePath (string): path to write the stego-open document
		data (string|bytes|<file>): data to encode
	"""
	# iterate xml files and inject data in chunks
	zipfile.encodeComment(openPath, writePath, data)


def decodeComment(openPath):
	"""decode data from a open document file by reading xml comments

	Args:
		openPath (string): path to the stego-open document to decode

	Returns:
		bytes: data from the image
	"""
	# iterate xml files and fetch comments - sort files alphanumerically
	return zipfile.decodeComment(openPath)


def encodeFile(openPath, writePath, file, fileName="application.xml",
password=""):
	""" encode data as a file """
	# Add one of the following: <manifest:manifest></manifest:manifest>
	# <manifest:file-entry manifest:full-path="<file>" manifest:media-type="application/octet-stream"/>
	# <manifest:file-entry manifest:full-path="/application.xml"
	# manifest:media-type="text/xml"/>
	copyfile(openPath, writePath)
	with MutableZipFile(writePath, "a", compression=ZIP_DEFLATED) as zipFile:
		zipFile.writestr(fileName, otp(toBin(file), password))
		with zipFile.open("META-INF/manifest.xml", "r") as xmlFile:
			lines = [line.strip() for line in xmlFile.readlines()]
		lines[1] = lines[1].replace(
		b"</manifest:manifest>", b"<manifest:file-entry manifest:full-path=\"" +
		fileName.encode("utf-8") + b"\" manifest:media-type=\"" + (b"text/xml"
		if fileName == "application.xml" else b"application/octet-stream") +
		b"\"/></manifest:manifest>")
		zipFile.writestr("META-INF/manifest.xml", b"\n".join(lines))


def decodeFile(openPath, password="", filePointer=None):
	""" decode data as a file """
	# Look for "/*.[* not .xml]" or "/application.xml"
	with ZipFile(openPath, "r", compression=ZIP_DEFLATED) as zipFile:
		files = []
		for file in zipFile.namelist():
			if not file.endswith(
			(".xml", "mimetype")) or file.endswith("application.xml"):
				files.append(file)
		with zipFile.open(files[0], "r") as dataFile:
			data = otp(dataFile.read(), password, False)
		return toFile(data, filePointer) if filePointer else data


def detectSteg(openPath):
	""" detect the use of odf steganography

	False positives can be triggered by including media in a document

	Args:
		openPath (string): path to the text file to analyse

	Returns:
		boolean: True if this lib has been used to hide data
	"""
	with ZipFile(openPath, "r", compression=ZIP_DEFLATED) as zipFile:
		files = []
		for file in zipFile.namelist():
			if not file.endswith(
			(".xml", "mimetype")) or file.endswith("application.xml"):
				files.append(file)
	return len(files) > 0 or zipfile.detectSteg(openPath)

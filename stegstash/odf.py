""" hide data and files in a odt, odp etc
Functions:
- Add data as a comment in xml such as META-INF/manifest.xml
- Add a file and update META-INF/manifest.xml
Limitations:
- These do not persist modification. i.e. the data will be lost in the event of
a user modifying the document (tested in LibreOffice and Microsoft Word 365:2004)
"""

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


def encodeFile(file):
	""" encode data as a file """
	# Add one of the following: <manifest:manifest></manifest:manifest>
	# <manifest:file-entry manifest:full-path="<file>" manifest:media-type="application/octet-stream"/>
	# <manifest:file-entry manifest:full-path="/application.xml"
	# manifest:media-type="text/xml"/>


def decodeFile():
	""" decode data as a file """
	# Look for "/*.[* not .xml]" or "/application.xml"

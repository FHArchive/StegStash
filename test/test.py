""" tests """
import sys
import os
from pathlib import Path
THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, os.path.dirname(THISDIR))

from stegstash import imagelsb, fileappend, soundlsb, homoglyphs, msoffice

# Simple imagelsb
imagelsb.simpleEncode(THISDIR + "/originalImage.png",
THISDIR + "/lsbSimpleEncode.png", "hello world from lsbSimpleEncode!")
print(imagelsb.simpleDecode(THISDIR + "/lsbSimpleEncode.png"))

# Hide image simplelsb
imagelsb.simpleEncode(THISDIR + "/originalImage.png",
THISDIR + "/lsbImageEncode.png", open(THISDIR + "/hideImage.png", "rb"))
imagelsb.simpleDecode(THISDIR + "/lsbImageEncode.png", False,
open(THISDIR + "/hideImageRecovered.png", "wb"))

# imagelsb
imagelsb.encode(THISDIR + "/originalImage.png", THISDIR + "/lsbEncode.png",
"hello world from lsbEncode!", "test", "pass")
print(imagelsb.decode(THISDIR + "/lsbEncode.png", "test", "pass"))

# imageappend
fileappend.encode(THISDIR + "/originalImage.png",
THISDIR + "/appendEncode.png", "hello world from appendEncode!", "pass")
print(fileappend.decode(THISDIR + "/appendEncode.png", "pass"))

# soundlsb
soundlsb.simpleEncode(THISDIR + "/originalSound.wav",
THISDIR + "/simpleEncode.wav", "hello world from soundLsbSimpleEncode!")
print(soundlsb.simpleDecode(THISDIR + "/simpleEncode.wav"))
soundlsb.encode(THISDIR + "/originalSound.wav", THISDIR + "/encode.wav",
"hello world from soundLsbEncode!", "test", "pass")
print(soundlsb.decode(THISDIR + "/encode.wav", "test", "pass"))

# homoglyphs
homoglyphs.simpleEncode(THISDIR + "/originalText.txt",
THISDIR + "/simpleEncode.txt", "glyph")
print(homoglyphs.simpleDecode(THISDIR + "/simpleEncode.txt"))

# MsOffice
msoffice.encodeComment(THISDIR + "/originalDoc.docx",
THISDIR + "/encodeComment.docx", "hello world from encodeComment!")
print(msoffice.decodeComment(THISDIR + "/encodeComment.docx"))
msoffice.encodeFile(THISDIR + "/originalDoc.docx",
THISDIR + "/encodeFile.docx", open(THISDIR + "/hideImage.png", "rb"), password="pass")
msoffice.decodeFile(THISDIR + "/encodeFile.docx", "pass",
open(THISDIR + "/docxImageRecovered.png", "wb"))

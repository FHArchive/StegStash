""" tests """
import sys
import os
from pathlib import Path
THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, os.path.dirname(THISDIR))

from stegstash import (imagelsb, fileappend, soundlsb, homoglyphs, msoffice, odf, zerowidth)

# Simple imagelsb
print("\n# simple imagelsb")
imagelsb.simpleEncode(THISDIR + "/originalImage.png",
THISDIR + "/lsbSimpleEncode.png", "hello world from lsbSimpleEncode!")
print(imagelsb.simpleDecode(THISDIR + "/lsbSimpleEncode.png"))
imagelsb.visual(THISDIR + "/originalImage.png", THISDIR + "/imagelsbVog.png")
imagelsb.visual(THISDIR + "/lsbSimpleEncode.png", THISDIR + "/imagelsbVen.png")

# Hide image simplelsb
print("\n# hide image simplelsb")
imagelsb.simpleEncode(THISDIR + "/originalImage.png",
THISDIR + "/lsbImageEncode.png", open(THISDIR + "/hideImage.png", "rb"))
imagelsb.simpleDecode(THISDIR + "/lsbImageEncode.png", False,
open(THISDIR + "/hideImageRecovered.png", "wb"))

# imagelsb
print("\n# imagelsb")
imagelsb.encode(THISDIR + "/originalImage.png", THISDIR + "/lsbEncode.png",
"hello world from lsbEncode!", "test", "pass")
print(imagelsb.decode(THISDIR + "/lsbEncode.png", "test", "pass"))

# fileappend
print("\n# fileappend")
fileappend.encode(THISDIR + "/originalImage.png",
THISDIR + "/appendEncode.png", "hello world from appendEncode!", "pass")
print(fileappend.decode(THISDIR + "/appendEncode.png", "pass"))
print(fileappend.detectSteg(THISDIR + "/originalImage.png"))
print(fileappend.detectSteg(THISDIR + "/appendEncode.png"))

# soundlsb
print("\n# soundlsb")
soundlsb.simpleEncode(THISDIR + "/originalSound.wav",
THISDIR + "/simpleEncode.wav", "hello world from soundLsbSimpleEncode!")
print(soundlsb.simpleDecode(THISDIR + "/simpleEncode.wav"))
soundlsb.encode(THISDIR + "/originalSound.wav", THISDIR + "/encode.wav",
"hello world from soundLsbEncode!", "test", "pass")
print(soundlsb.decode(THISDIR + "/encode.wav", "test", "pass"))

# homoglyphs
print("\n# homoglyphs")
homoglyphs.simpleEncode(THISDIR + "/originalText.txt",
THISDIR + "/simpleEncode.txt", "glyph")
print(homoglyphs.simpleDecode(THISDIR + "/simpleEncode.txt"))
homoglyphs.encode(THISDIR + "/originalText.txt",
THISDIR + "/encode.txt", "glyph", "test", "pass")
print(homoglyphs.decode(THISDIR + "/encode.txt", "test", "pass"))
print(homoglyphs.detectSteg(THISDIR + "/originalText.txt"))
print(homoglyphs.detectSteg(THISDIR + "/encode.txt"))
homoglyphs.visual(THISDIR + "/originalText.txt", THISDIR + "/homoglyphsVog.png")
homoglyphs.visual(THISDIR + "/encode.txt", THISDIR + "/homoglyphsVen.png")

# MsOffice
print("\n# msoffice")
msoffice.encodeComment(THISDIR + "/originalDoc.docx",
THISDIR + "/encodeComment.docx", "hello world from encodeComment!")
print(msoffice.decodeComment(THISDIR + "/encodeComment.docx"))
msoffice.encodeFile(THISDIR + "/originalDoc.docx",
THISDIR + "/encodeFile.docx", open(THISDIR + "/hideImage.png", "rb"), password="pass")
msoffice.decodeFile(THISDIR + "/encodeFile.docx", "pass",
open(THISDIR + "/docxImageRecovered.png", "wb"))
print(msoffice.detectSteg(THISDIR + "/originalDoc.docx"))
print(msoffice.detectSteg(THISDIR + "/encodeFile.docx"))

# odt
print("\n# odt")
odf.encodeComment(THISDIR + "/originalDoc.odt",
THISDIR + "/encodeComment.odt", "hello world from encodeComment odt!")
print(odf.decodeComment(THISDIR + "/encodeComment.odt"))
odf.encodeFile(THISDIR + "/originalDoc.odt",
THISDIR + "/encodeFile.odt", open(THISDIR + "/hideImage.png", "rb"), password="pass")
odf.decodeFile(THISDIR + "/encodeFile.odt", "pass",
open(THISDIR + "/odtImageRecovered.png", "wb"))
print(odf.detectSteg(THISDIR + "/originalDoc.odt"))
print(odf.detectSteg(THISDIR + "/encodeFile.odt"))

# zerowidth
print("\n# zerowidth")
zerowidth.simpleEncode(THISDIR + "/originalText.txt",
THISDIR + "/simpleEncodeZW.txt", "zerowidth")
print(zerowidth.simpleDecode(THISDIR + "/simpleEncodeZW.txt"))
zerowidth.encode(THISDIR + "/originalText.txt",
THISDIR + "/encodeZW.txt", "zerowidth", "test", "pass")
print(zerowidth.decode(THISDIR + "/encodeZW.txt", "test", "pass"))
print(zerowidth.detectSteg(THISDIR + "/originalText.txt"))
print(zerowidth.detectSteg(THISDIR + "/simpleEncodeZW.txt"))
zerowidth.visual(THISDIR + "/originalText.txt", THISDIR + "/zerowidthVog.png")
zerowidth.visual(THISDIR + "/encodeZW.txt", THISDIR + "/zerowidthVen.png")

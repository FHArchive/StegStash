""" tests """

import sys
import os
from pathlib import Path
THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, os.path.dirname(THISDIR))

from stegstash import imagelsb, fileappend, soundlsb, homoglyphs

# Simple imagelsb
imagelsb.simpleEncode(THISDIR + "/originalImage.png", THISDIR + "/lsbSimpleEncode.png",
"hello world from lsbSimpleEncode!")
print(imagelsb.simpleDecode(THISDIR + "/lsbSimpleEncode.png"))

# imagelsb
imagelsb.encode(THISDIR + "/originalImage.png", THISDIR + "/lsbEncode.png",
"hello world from lsbEncode!", "test", "pass")
print(imagelsb.decode(THISDIR + "/lsbEncode.png", "test", "pass"))

# imageappend
fileappend.encode(THISDIR + "/originalImage.png", THISDIR + "/appendEncode.png",
"hello world from appendEncode!", "pass")
print(fileappend.decode(THISDIR + "/appendEncode.png", "pass"))

# soundlsb - doesn't work!
soundlsb.simpleEncode(THISDIR + "/originalSound.wav", THISDIR + "/simpleEncode.wav",
"hello world from soundLsbSimpleEncode!")
print(soundlsb.simpleDecode(THISDIR + "/simpleEncode.wav"))

# homoglyphs
homoglyphs.simpleEncode(THISDIR + "/originalText.txt", THISDIR + "/simpleEncode.txt",
"glyph")
print(homoglyphs.simpleDecode(THISDIR + "/simpleEncode.txt"))

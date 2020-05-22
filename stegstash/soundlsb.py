""" from wikipedia
"""
import numpy as np
import soundfile as sf
from metprint import LogType, Logger, FHFormatter
from stegstash.lsb import LSB

exts = ["wav"]


def extNotLossless(fileName):
	""" Output the file extension not lossless error """
	Logger(FHFormatter()).logPrint(
	"File extension is not lossless: " + fileName + "! Must be " + "one of \"" +
	", \"".join(exts) + "\"", LogType.ERROR)


def encode(openPath, writePath, chars, imageMapSeed, password=""):
	""" encode a sound file with lsb data """
	data, samplerate, shape = openSound(openPath)
	encodeLsb = LSB(data, data=chars)
	data = encodeLsb.encode(imageMapSeed, password)
	writeSound(writePath, data, samplerate, shape)


def decode(openPath, imageMapSeed, password="", zeroTerm=True, file=None):
	""" decode a sound file and return a byte string """
	data, _samplerate, _shape = openSound(openPath)
	decodeLsb = LSB(data)
	return decodeLsb.decode(imageMapSeed, password, zeroTerm, file)


def simpleEncode(openPath, writePath, chars):
	""" encode a sound file with lsb data """
	data, samplerate, shape = openSound(openPath)
	encodeLsb = LSB(data, data=chars)
	data = encodeLsb.encodeSimpleFlatArr()
	writeSound(writePath, data, samplerate, shape)


def simpleDecode(openPath, zeroTerm=True, file=None):
	""" decode a sound file and return a byte string """
	data, _samplerate, _shape = openSound(openPath)
	decodeLsb = LSB(data)
	return decodeLsb.decodeSimpleFlatArr(zeroTerm, file)


def openSound(path):
	""" open a sound file """
	fileExt = path.split(".")[-1].lower()
	if fileExt not in exts:
		extNotLossless(path)
		raise ValueError
	data, samplerate = sf.read(path, always_2d=True, dtype='int16')
	return (data.flatten() + 2**15).astype(np.uint16), samplerate, data.shape


def writeSound(path, sound, samplerate, shape):
	""" save a sound file """
	fileExt = path.split(".")[-1].lower()
	if fileExt not in exts:
		extNotLossless(path)
		raise ValueError
	sound = (sound - 2**15).astype(np.int16)
	sf.write(path, sound.reshape(shape), samplerate)

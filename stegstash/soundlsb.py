""" LSB for Sound """
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


def encode(openPath, writePath, chars, soundMapSeed, password=""):
	"""encode a sound file with data using lsb steganography

	Args:
		openPath (string): path to the original sound file to open
		writePath (string): path to write the stego-sound file
		data (string|bytes|<file>): data to encode
		soundMapSeed (string): seed to generate the lsb map
		password (str, optional): password to encrypt the data with. Defaults to "".
	"""
	data, samplerate, shape = openSound(openPath)
	encodeLsb = LSB(data, data=chars)
	data = encodeLsb.encode(soundMapSeed, password)
	writeSound(writePath, data, samplerate, shape)


def decode(openPath, soundMapSeed, password="", zeroTerm=True, file=None):
	"""decode data from a sound file using lsb steganography

	Args:
		openPath (string): path to the stego-sound file to decode
		soundMapSeed (string): seed to generate the lsb map
		password (str, optional): password to encrypt the data with. Defaults to "".
		zeroTerm (boolean, optional): stop decoding on \x00 (NUL). Defaults to True.
		file (<file>, optional): file pointer. Defaults to None.

	Returns:
		bytes: data from the sound file
	"""
	data, _samplerate, _shape = openSound(openPath)
	decodeLsb = LSB(data)
	return decodeLsb.decode(soundMapSeed, password, zeroTerm, file)


def simpleEncode(openPath, writePath, chars):
	"""encode a sound file with data using lsb steganography

	Args:
		openPath (string): path to the original sound file to open
		writePath (string): path to write the stego-sound file
		data (string|bytes|<file>): data to encode
	"""
	data, samplerate, shape = openSound(openPath)
	encodeLsb = LSB(data, data=chars)
	data = encodeLsb.simpleEncode()
	writeSound(writePath, data, samplerate, shape)


def simpleDecode(openPath, zeroTerm=True, file=None):
	"""decode data from a sound file using lsb steganography

	Args:
		openPath (string): path to the stego-sound file to decode
		zeroTerm (boolean, optional): stop decoding on \x00 (NUL). Defaults to True.
		file (<file>, optional): file pointer. Defaults to None.

	Returns:
		bytes: data from the sound file
	"""
	data, _samplerate, _shape = openSound(openPath)
	decodeLsb = LSB(data)
	return decodeLsb.simpleDecode(zeroTerm, file)


def openSound(path):
	""" open a sound file """
	"""Open a sound file as a numpy array

	Args:
		path (string): path to the sound file to open

	Returns:
		numpy.array, int, Tuple(int): A 1D numpy array containing sound data,
		 sample rate, shape
	"""
	fileExt = path.split(".")[-1].lower()
	if fileExt not in exts:
		extNotLossless(path)
		raise ValueError
	data, samplerate = sf.read(path, always_2d=True, dtype='int16')
	return (data.flatten() + 2**15).astype(np.uint16), samplerate, data.shape


def writeSound(path, sound, samplerate, shape):
	"""Write a 1D numpy array to a sound file

	Args:
		path (string): path to the sound file to save
		sound (numpy.array): 1D numpy array containing sound data
		samplerate int: sample rate
		shape (Tuple(int)): shape
	"""
	fileExt = path.split(".")[-1].lower()
	if fileExt not in exts:
		extNotLossless(path)
		raise ValueError
	sound = (sound - 2**15).astype(np.int16)
	sf.write(path, sound.reshape(shape), samplerate)

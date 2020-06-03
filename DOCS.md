<a name=".make"></a>
## make

Makefile for python. Run one of the following subcommands:

install: Poetry install
build: Building docs, requirements.txt, setup.py, poetry build
security: Run some basic security checks that are not run in vscode

<a name=".stegstash"></a>
## stegstash

Provides multiple methods to hide and retrieve data.

<a name=".stegstash.fileappend"></a>
## stegstash.fileappend

append data to an image after the end
Files and byte(s) terminators

jpg: \xff\xd9
png: \x49\x45\x4e\x44\xae\x42\x60\x82 (IEND.b`. - think only IEND is required)
gif: \x00\x3b (\x3b according to wikipedia)

<a name=".stegstash.fileappend.extNotSupported"></a>
#### extNotSupported

```python
extNotSupported(fileName)
```

Output the file extension not supported error

<a name=".stegstash.fileappend.encode"></a>
#### encode

```python
encode(openPath, writePath, appendData, password="")
```

encode a file with data by appending binary after the end of the file

**Arguments**:

- `openPath` _string_ - path to the original file to open
- `writePath` _string_ - path to write the stego-file
- `appendData` _string|bytes|<file>_ - data to encode
- `password` _str, optional_ - password to encrypt the data with. Defaults to "".

<a name=".stegstash.fileappend.decode"></a>
#### decode

```python
decode(openPath, password="", file=None)
```

decode data from a file by extracting data after end of file

**Arguments**:

- `openPath` _string_ - path to the stego-file to decode
- `password` _str, optional_ - password to encrypt the data with. Defaults to "".
- `file` _<file>, optional_ - file pointer. Defaults to None.
  

**Returns**:

- `bytes` - data from the image

<a name=".stegstash.fileappend.openFile"></a>
#### openFile

```python
openFile(path)
```

Open an file to bytes

**Arguments**:

- `path` _string_ - path to the file to open
  

**Returns**:

- `bytes` - file data

<a name=".stegstash.fileappend.writeFile"></a>
#### writeFile

```python
writeFile(path, byteArr)
```

Write bytes to a file

**Arguments**:

- `path` _string_ - path to the file to save
- `byteArr` _bytes_ - bytes to write to the file

<a name=".stegstash.fileappend.detectSteg"></a>
#### detectSteg

```python
detectSteg(openPath)
```

detect the use of file appended steganography

**Arguments**:

- `openPath` _string_ - path to the text file to analyse
  

**Returns**:

- `boolean` - True if this lib has been used to hide data

<a name=".stegstash.homoglyphs"></a>
## stegstash.homoglyphs

encode a text file using homoglyphs

<a name=".stegstash.homoglyphs.simpleEncode"></a>
#### simpleEncode

```python
simpleEncode(openPath, writePath, data)
```

encode a text file with data using homoglyphs

**Arguments**:

- `openPath` _string_ - path to the original text file to open
- `writePath` _string_ - path to write the stego-text file
- `data` _string|bytes|<file>_ - data to encode

<a name=".stegstash.homoglyphs.simpleDecode"></a>
#### simpleDecode

```python
simpleDecode(openPath, zeroTerm=True, file=None)
```

decode data from an text file using homoglyphs

**Arguments**:

- `openPath` _string_ - path to the stego-text file to decode
- `zeroTerm` _boolean, optional_ - stop decoding on \x00 (NUL). Defaults to True.
- `file` _<file>, optional_ - file pointer. Defaults to None.
  

**Returns**:

- `bytes` - data from the text file

<a name=".stegstash.homoglyphs.encode"></a>
#### encode

```python
encode(openPath, writePath, data, mapSeed, password="")
```

encode a text file with data using homoglyphs

**Arguments**:

- `openPath` _string_ - path to the original text file to open
- `writePath` _string_ - path to write the stego-text file
- `data` _string_ - data to encode
- `mapSeed` _string_ - seed to generate the lsb map
- `password` _str, optional_ - password to encrypt the data with. Defaults to "".

<a name=".stegstash.homoglyphs.decode"></a>
#### decode

```python
decode(openPath, mapSeed, password="", zeroTerm=True, file=None)
```

decode data from an text file using homoglyphs

**Arguments**:

- `openPath` _string_ - path to the stego-text file to decode
- `mapSeed` _string_ - seed to generate the lsb map
- `password` _str, optional_ - password to encrypt the data with. Defaults to "".
- `zeroTerm` _boolean, optional_ - stop decoding on \x00 (NUL). Defaults to True.
- `file` _<file>, optional_ - file pointer. Defaults to None.
  

**Returns**:

- `bytes` - data from the text file

<a name=".stegstash.homoglyphs.encodeGlyph"></a>
#### encodeGlyph

```python
encodeGlyph(fileData, position, byte, shift)
```

encode a single glyph (1/8th of hidden data)

<a name=".stegstash.homoglyphs.decodeGlyph"></a>
#### decodeGlyph

```python
decodeGlyph(fileData, position, byte, shift)
```

decode a single glyph (1/8th of hidden data)

<a name=".stegstash.homoglyphs.detectSteg"></a>
#### detectSteg

```python
detectSteg(openPath)
```

Detect the use of homoglyph stegonography.

False positives can be easily triggered (this checks for non ascii chars)

**Arguments**:

- `openPath` _string_ - path to the text file to analyse
  

**Returns**:

- `boolean` - True if this lib has been used to hide data

<a name=".stegstash.imagelsb"></a>
## stegstash.imagelsb

encode and decode methods

<a name=".stegstash.imagelsb.extNotLossless"></a>
#### extNotLossless

```python
extNotLossless(fileName)
```

Output the file extension not lossless error

<a name=".stegstash.imagelsb.encode"></a>
#### encode

```python
encode(openPath, writePath, data, imageMapSeed, password="")
```

encode an image with data using lsb steganography

**Arguments**:

- `openPath` _string_ - path to the original image to open
- `writePath` _string_ - path to write the stego-image
- `data` _string|bytes|<file>_ - data to encode
- `imageMapSeed` _string_ - seed to generate the lsb map
- `password` _str, optional_ - password to encrypt the data with. Defaults to "".

<a name=".stegstash.imagelsb.decode"></a>
#### decode

```python
decode(openPath, imageMapSeed, password="", zeroTerm=True, file=None)
```

decode data from an image using lsb steganography

**Arguments**:

- `openPath` _string_ - path to the stego-image to decode
- `imageMapSeed` _string_ - seed to generate the lsb map
- `password` _str, optional_ - password to encrypt the data with. Defaults to "".
- `zeroTerm` _boolean, optional_ - stop decoding on \x00 (NUL). Defaults to True.
- `file` _<file>, optional_ - file pointer. Defaults to None.
  

**Returns**:

- `bytes` - data from the image

<a name=".stegstash.imagelsb.simpleEncode"></a>
#### simpleEncode

```python
simpleEncode(openPath, writePath, data)
```

encode an image with data using lsb steganography

**Arguments**:

- `openPath` _string_ - path to the original image to open
- `writePath` _string_ - path to write the stego-image
- `data` _string|bytes|<file>_ - data to encode

<a name=".stegstash.imagelsb.simpleDecode"></a>
#### simpleDecode

```python
simpleDecode(openPath, zeroTerm=True, file=None)
```

decode data from an image using lsb steganography

**Arguments**:

- `openPath` _string_ - path to the stego-image to decode
- `zeroTerm` _boolean, optional_ - stop decoding on \x00 (NUL). Defaults to True.
- `file` _<file>, optional_ - file pointer. Defaults to None.
  

**Returns**:

- `bytes` - data from the image

<a name=".stegstash.imagelsb.openImg"></a>
#### openImg

```python
openImg(path)
```

Open an image as a numpy array

**Arguments**:

- `path` _string_ - path to the image to open
  

**Returns**:

  numpy.array, (int, int), string: A 1D numpy array containing image
  pixels, image size, image mode

<a name=".stegstash.imagelsb.writeImg"></a>
#### writeImg

```python
writeImg(path, image, imageSize, mode)
```

Write a 1D numpy array to a file

**Arguments**:

- `path` _string_ - path to the image to save
- `image` _numpy.array_ - 1D numpy array containing image pixels
  imageSize ((int, int)): size of the image
- `mode` _string_ - PIL Image mode typically one of "RGBA", "RGB", "PA", "P"

<a name=".stegstash.lsb"></a>
## stegstash.lsb

common lsb functions

<a name=".stegstash.lsb.LSB"></a>
### LSB

```python
class LSB():
 |  LSB(array, pointer=0, data=None)
```

Perform lsb encoding and decoding on an array

<a name=".stegstash.lsb.LSB.setLsb"></a>
#### setLsb

```python
 | setLsb(bit)
```

set lsb

<a name=".stegstash.lsb.LSB.getLsb"></a>
#### getLsb

```python
 | getLsb()
```

get lsb

<a name=".stegstash.lsb.LSB.setLsb8"></a>
#### setLsb8

```python
 | setLsb8(byte)
```

set lsb8

<a name=".stegstash.lsb.LSB.getLsb8"></a>
#### getLsb8

```python
 | getLsb8()
```

get lsb8

<a name=".stegstash.lsb.LSB.setLsb8C"></a>
#### setLsb8C

```python
 | setLsb8C(char)
```

set lsb8 char

<a name=".stegstash.lsb.LSB.getLsb8C"></a>
#### getLsb8C

```python
 | getLsb8C()
```

get lsb8 char

<a name=".stegstash.lsb.LSB.simpleDecode"></a>
#### simpleDecode

```python
 | simpleDecode(zeroTerm=True, file=None)
```

decode a flat array with no encryption

**Arguments**:

- `zeroTerm` _boolean, optional_ - stop decoding on \x00 (NUL). Defaults to True.
- `file` _<file>, optional_ - file pointer. Defaults to None.

<a name=".stegstash.lsb.LSB.simpleEncode"></a>
#### simpleEncode

```python
 | simpleEncode()
```

encode a flat array with no encryption

<a name=".stegstash.lsb.LSB.decode"></a>
#### decode

```python
 | decode(mapSeed, password="", zeroTerm=True, file=None)
```

decode data from an array using lsb steganography

**Arguments**:

- `mapSeed` _string_ - seed to generate the lsb map
- `password` _str, optional_ - password to encrypt the data with. Defaults to "".
- `zeroTerm` _boolean, optional_ - stop decoding on \x00 (NUL). Defaults to True.
- `file` _<file>, optional_ - file pointer. Defaults to None.
  

**Returns**:

- `bytes` - data from the image

<a name=".stegstash.lsb.LSB.encode"></a>
#### encode

```python
 | encode(mapSeed, password="")
```

encode an array with data using lsb steganography

**Arguments**:

- `mapSeed` _string_ - seed to generate the lsb map
- `password` _str, optional_ - password to encrypt the data with. Defaults to "".

<a name=".stegstash.msoffice"></a>
## stegstash.msoffice

hide data and files in a docx, pptx etc
Functions:
- Add data as a comment in xml such as [Content_Types].xml
- Add a file and update [Content_Types].xml
Limitations:
- These do not persist modification. i.e. the data will be lost in the event of
a user modifying the document (tested in LibreOffice and Microsoft Word 365:2004)

<a name=".stegstash.msoffice.encodeComment"></a>
#### encodeComment

```python
encodeComment(openPath, writePath, data)
```

encode an microsoft office file with data by inserting into xml comments

**Arguments**:

- `openPath` _string_ - path to the original office document to open
- `writePath` _string_ - path to write the stego-office document
- `data` _string|bytes|<file>_ - data to encode

<a name=".stegstash.msoffice.decodeComment"></a>
#### decodeComment

```python
decodeComment(openPath)
```

decode data from a microsoft office file by reading xml comments

**Arguments**:

- `openPath` _string_ - path to the stego-office document to decode
  

**Returns**:

- `bytes` - data from the image

<a name=".stegstash.msoffice.encodeFile"></a>
#### encodeFile

```python
encodeFile(openPath, writePath, file, fileName="application.xml", password="")
```

encode data as a file

<a name=".stegstash.msoffice.decodeFile"></a>
#### decodeFile

```python
decodeFile(openPath, password="", filePointer=None)
```

decode data from a microsoft office file by extracting the file

**Arguments**:

- `openPath` _string_ - path to the stego-document to decode
- `password` _str, optional_ - password to encrypt the data with. Defaults to "".
- `filePointer` _<file>, optional_ - pointer to the file. Defaults to None.
  

**Returns**:

- `bytes` - data from the image

<a name=".stegstash.msoffice.detectSteg"></a>
#### detectSteg

```python
detectSteg(openPath, checkDocPropsOnly=True)
```

detect the use of microsoft office steganography

False positives can be triggered by including media in a document when
checkDocPropsOnly is set to False

**Arguments**:

- `openPath` _string_ - path to the text file to analyse
- `checkDocPropsOnly` _boolean, optional_ - look under docProps only to
  mitigate one source of false positives. Defaults to True.
  

**Returns**:

- `boolean` - True if this lib has been used to hide data

<a name=".stegstash.odf"></a>
## stegstash.odf

hide data and files in a odt, odp etc
Functions:
- Add data as a comment in xml such as META-INF/manifest.xml
- Add a file and update META-INF/manifest.xml
Limitations:
- These do not persist modification. i.e. the data will be lost in the event of
a user modifying the document (tested in LibreOffice and Microsoft Word 365:2004)

<a name=".stegstash.odf.encodeComment"></a>
#### encodeComment

```python
encodeComment(openPath, writePath, data)
```

encode an open document file with data by inserting into xml comments

**Arguments**:

- `openPath` _string_ - path to the original open document to open
- `writePath` _string_ - path to write the stego-open document
- `data` _string|bytes|<file>_ - data to encode

<a name=".stegstash.odf.decodeComment"></a>
#### decodeComment

```python
decodeComment(openPath)
```

decode data from a open document file by reading xml comments

**Arguments**:

- `openPath` _string_ - path to the stego-open document to decode
  

**Returns**:

- `bytes` - data from the image

<a name=".stegstash.odf.encodeFile"></a>
#### encodeFile

```python
encodeFile(openPath, writePath, file, fileName="application.xml", password="")
```

encode data as a file

<a name=".stegstash.odf.decodeFile"></a>
#### decodeFile

```python
decodeFile(openPath, password="", filePointer=None)
```

decode data as a file

<a name=".stegstash.odf.detectSteg"></a>
#### detectSteg

```python
detectSteg(openPath)
```

detect the use of odf steganography

False positives can be triggered by including media in a document

**Arguments**:

- `openPath` _string_ - path to the text file to analyse
  

**Returns**:

- `boolean` - True if this lib has been used to hide data

<a name=".stegstash.soundlsb"></a>
## stegstash.soundlsb

LSB for Sound

<a name=".stegstash.soundlsb.extNotLossless"></a>
#### extNotLossless

```python
extNotLossless(fileName)
```

Output the file extension not lossless error

<a name=".stegstash.soundlsb.encode"></a>
#### encode

```python
encode(openPath, writePath, chars, soundMapSeed, password="")
```

encode a sound file with data using lsb steganography

**Arguments**:

- `openPath` _string_ - path to the original sound file to open
- `writePath` _string_ - path to write the stego-sound file
- `data` _string|bytes|<file>_ - data to encode
- `soundMapSeed` _string_ - seed to generate the lsb map
- `password` _str, optional_ - password to encrypt the data with. Defaults to "".

<a name=".stegstash.soundlsb.decode"></a>
#### decode

```python
decode(openPath, soundMapSeed, password="", zeroTerm=True, file=None)
```

decode data from a sound file using lsb steganography

**Arguments**:

- `openPath` _string_ - path to the stego-sound file to decode
- `soundMapSeed` _string_ - seed to generate the lsb map
- `password` _str, optional_ - password to encrypt the data with. Defaults to "".
- `zeroTerm` _boolean, optional_ - stop decoding on \x00 (NUL). Defaults to True.
- `file` _<file>, optional_ - file pointer. Defaults to None.
  

**Returns**:

- `bytes` - data from the sound file

<a name=".stegstash.soundlsb.simpleEncode"></a>
#### simpleEncode

```python
simpleEncode(openPath, writePath, chars)
```

encode a sound file with data using lsb steganography

**Arguments**:

- `openPath` _string_ - path to the original sound file to open
- `writePath` _string_ - path to write the stego-sound file
- `data` _string|bytes|<file>_ - data to encode

<a name=".stegstash.soundlsb.simpleDecode"></a>
#### simpleDecode

```python
simpleDecode(openPath, zeroTerm=True, file=None)
```

decode data from a sound file using lsb steganography

**Arguments**:

- `openPath` _string_ - path to the stego-sound file to decode
- `zeroTerm` _boolean, optional_ - stop decoding on \x00 (NUL). Defaults to True.
- `file` _<file>, optional_ - file pointer. Defaults to None.
  

**Returns**:

- `bytes` - data from the sound file

<a name=".stegstash.soundlsb.openSound"></a>
#### openSound

```python
openSound(path)
```

open a sound file

<a name=".stegstash.soundlsb.writeSound"></a>
#### writeSound

```python
writeSound(path, sound, samplerate, shape)
```

Write a 1D numpy array to a sound file

**Arguments**:

- `path` _string_ - path to the sound file to save
- `sound` _numpy.array_ - 1D numpy array containing sound data
  samplerate int: sample rate
  shape (Tuple(int)): shape

<a name=".stegstash.utils"></a>
## stegstash.utils

utility functions

<a name=".stegstash.utils.charsToBin"></a>
#### charsToBin

```python
charsToBin(chars)
```

convert a sequence of chars to binary

<a name=".stegstash.utils.binToChars"></a>
#### binToChars

```python
binToChars(data)
```

convert binary to a sequence of chars

<a name=".stegstash.utils.toBin"></a>
#### toBin

```python
toBin(data)
```

convert one of chars| bin| file to bin

<a name=".stegstash.utils.toChars"></a>
#### toChars

```python
toChars(data)
```

convert one of chars| bin| file to chars

<a name=".stegstash.utils.toFile"></a>
#### toFile

```python
toFile(data, file)
```

convert one of chars| bin| file to file

<a name=".stegstash.utils.getMap"></a>
#### getMap

```python
getMap(array, seed)
```

get an array map from a seed using python's predictable number generator,
Isn't security wonderful

<a name=".stegstash.utils.otp"></a>
#### otp

```python
otp(data, password, encodeFlag=True)
```

do one time pad encoding on a sequence of chars

<a name=".stegstash.utils.otpChars"></a>
#### otpChars

```python
otpChars(data, password, encodeFlag=True)
```

do one time pad encoding on a sequence of chars

<a name=".stegstash.zerowidth"></a>
## stegstash.zerowidth

Uses zero width chars to hide data

One similar project uses the following code points:
Unicode u200b to u200f
zero width space
zero width non joiner
zero width joiner
left to right mark
right to left mark

These are invisible in VSCode, Notepad.exe and PythonIDLE

See the table below for a comparison of various glyphs in a series of popular text
editors

|Char Code|   Char Name|Notepad.exe|VSCode|PythonIDLE|KWrite|EMACS|<safe>|MsWord|    Utf8|
|---------|------------|-----------|------|----------|------|-----|------|------|--------|
|<control>|   <control>|          x|     x|         x|     x|    x|     x|     x|        |
|u00ad    |  SoffHyphen|          x|     +|         x|     x|    x|     x|     x|        |
|u034f    |   CombiningGraphemeJoiner|+| +|         +|     +|    x|     x|     +|        |
|u200b    |     ZWSpace|          +|     +|         +|     +|    +|     +|     +|E2 80 8B|
|u200c    | ZWNonJoiner|          +|     +|         +|     +|    +|     +|     +|E2 80 8C|
|u200d    |    ZWJoiner|          +|     +|         +|     +|    +|     +|     +|E2 80 8D|
|u200e    |     LTRMark|          +|     +|         +|     +|    +|     +|     +|E2 80 8E|
|u200f    |     RTLMark|          +|     +|         +|     +|    +|     +|     +|E2 80 8F|
|u202a    |LTREmbedding|          +|     +|         +|     +|    +|     +|     +|E2 80 AA|
|u202b    |RTLEmbedding|          +|     +|         +|     +|    +|     +|     +|        |
|u202c    |  PopDirectionalFormatting|+| +|         +|     +|    +|     +|     +|E2 80 AC|
|u202d    | LTROverride|          +|     +|         +|     +|    +|     +|     +|E2 80 AD|
|u202e    | RTLOverride|          x|     x|         +|     x|    x|     x|     x|        |
|u2060    |  WordJoiner|          x|     +|         +|     +|    +|     x|     +|        |
|u2061    |   FunctionApplication|+|     +|         +|     +|    +|     +|     x|E2 81 A1|
|u2062    |        InvisibleTimes|+|     +|         +|     +|    +|     +|     x|E2 81 A2|
|u2063    |    InvisibleSeperator|+|     +|         +|     +|    +|     +|     x|E2 81 A3|
|u2064    |InvisiblePlue|         +|     +|         +|     +|    +|     +|     x|E2 81 A4|
|u2065    |   <unknown>|          x|     +|         x|     +|    x|     x|     x|        |
|u2066    |  LTRIsolate|          x|     +|         x|     +|    +|     x|     x|        |
|u2067    |  RTLIsolate|          x|     +|         x|     +|    +|     x|     x|        |
|u2068    |    FirstStrongIsolate|x|     +|         x|     +|    +|     x|     x|        |
|u2069    | PopDirectionalIsolate|x|     +|         x|     +|    +|     x|     x|        |
|u206a    |  InhibitSymmetricSwapping|+| +|         +|     +|    +|     +|     x|E2 81 AA|
|u206b    | ActivateSymmetricSwapping|+| +|         +|     +|    +|     +|     x|E2 81 AB|
|u206c    | InhibitArabicFormSwapping|+| +|         +|     +|    +|     +|     x|E2 81 AC|
|u206d    |ActivateArabicFormSwapping|+| +|         +|     +|    +|     +|     x|E2 81 AD|
|u206e    |   NationalDigitShapes|+|     +|         +|     +|    +|     +|     x|E2 81 AE|
|u206f    |    NominalDigitShapes|+|     +|         +|     +|    +|     +|     x|E2 81 AF|
|u2068    |    FirstStrongIsolate|x|     +|         x|     +|    +|     x|     x|        |

The likes of vim/gvim show these up but a typical user is unlikely to be using
those text editors.

Though not a text editor, Microsoft Word seems pretty good at higlighting some
of these chars (at least better than initially expected). There is a possibility
that a user may have configured word to open a text file (though not completely
likely). To mitigate this slim risk a safe mode will be added to disable use of
these chars

<a name=".stegstash.zerowidth.encode"></a>
#### encode

```python
encode(openPath, writePath, data, mapSeed, password="", safe=True)
```

encode a text file with data using zero width chars

**Arguments**:

- `openPath` _string_ - path to the original text file to open
- `writePath` _string_ - path to write the stego-text file
- `data` _string|bytes|<file>_ - data to encode
- `mapSeed` _string_ - seed to generate the lsb map
- `password` _str, optional_ - password to encrypt the data with. Defaults to "".
- `safe` _boolean, optional_ - use a reduced set of chars to show in fewer
  editors. Defaults to True.

<a name=".stegstash.zerowidth.decode"></a>
#### decode

```python
decode(openPath, mapSeed, password="", zeroTerm=True, file=None, safe=True)
```

decode data from a text file using zero width chars

**Arguments**:

- `openPath` _string_ - path to the stego-text file to decode
- `mapSeed` _string_ - seed to generate the lsb map
- `password` _str, optional_ - password to encrypt the data with. Defaults to "".
- `zeroTerm` _boolean, optional_ - stop decoding on \x00 (NUL). Defaults to True.
- `file` _<file>, optional_ - file pointer. Defaults to None.
- `safe` _boolean, optional_ - use a reduced set of chars to show in fewer
  editors. Defaults to True.
  

**Returns**:

- `bytes` - data from the text file

<a name=".stegstash.zerowidth.simpleEncode"></a>
#### simpleEncode

```python
simpleEncode(openPath, writePath, data, safe=True)
```

encode a text file with data using zero width chars

**Arguments**:

- `openPath` _string_ - path to the original text file to open
- `writePath` _string_ - path to write the stego-text file
- `data` _string|bytes|<file>_ - data to encode
- `safe` _boolean, optional_ - use a reduced set of chars to show in fewer
  editors. Defaults to True.

<a name=".stegstash.zerowidth.simpleDecode"></a>
#### simpleDecode

```python
simpleDecode(openPath, zeroTerm=True, file=None, safe=True)
```

decode data from a text file using zero width chars

**Arguments**:

- `openPath` _string_ - path to the stego-text file to decode
- `zeroTerm` _boolean, optional_ - stop decoding on \x00 (NUL). Defaults to True.
- `file` _<file>, optional_ - file pointer. Defaults to None.
- `safe` _boolean, optional_ - use a reduced set of chars to show in fewer
  editors. Defaults to True.
  

**Returns**:

- `bytes` - data from the text file

<a name=".stegstash.zerowidth.encodeCharZero"></a>
#### encodeCharZero

```python
encodeCharZero(fileData, pointer, char, safe=True)
```

encode a char as a series of zero width chars such that the result looks
like foobar -> f\0o\0o\0bar

<a name=".stegstash.zerowidth.decodeCharZero"></a>
#### decodeCharZero

```python
decodeCharZero(fileData, pointer, safe=True)
```

decode a series of zero width chars as a char such that \0 is read
from f\0o\0o\0bar

<a name=".stegstash.zerowidth.writeUtf8"></a>
#### writeUtf8

```python
writeUtf8(pointer, newBytes, byteStream)
```

write a series of utf8 bytes after an existing char and advance the
pointer

<a name=".stegstash.zerowidth.readUtf8"></a>
#### readUtf8

```python
readUtf8(pointer, byteStream)
```

read the next zero char and advance the pointer
1 utf8: 0
2 utf8: 110
3 utf8: 1110
4 utf8: 11110

<a name=".stegstash.zerowidth.getUtf8Size"></a>
#### getUtf8Size

```python
getUtf8Size(byteStream, pointer)
```

get the size of the next utf8 char

<a name=".stegstash.zerowidth.detectSteg"></a>
#### detectSteg

```python
detectSteg(openPath)
```

detect the use of zero width char steganography

**Arguments**:

- `openPath` _string_ - path to the text file to analyse
  

**Returns**:

- `boolean` - True if this lib has been used to hide data

<a name=".stegstash.zipfile"></a>
## stegstash.zipfile

common zip steganography functions

<a name=".stegstash.zipfile.encodeComment"></a>
#### encodeComment

```python
encodeComment(openPath, writePath, data)
```

encode an microsoft office file with data by inserting into xml comments

**Arguments**:

- `openPath` _string_ - path to the original office document to open
- `writePath` _string_ - path to write the stego-office document
- `data` _string|bytes|<file>_ - data to encode

<a name=".stegstash.zipfile.decodeComment"></a>
#### decodeComment

```python
decodeComment(openPath)
```

decode data from a microsoft office file by reading xml comments

**Arguments**:

- `openPath` _string_ - path to the stego-office document to decode
  

**Returns**:

- `bytes` - data from the image

<a name=".stegstash.zipfile.detectSteg"></a>
#### detectSteg

```python
detectSteg(openPath)
```

detect the use of xml comment steganography using this library

**Arguments**:

- `openPath` _string_ - path to the text file to analyse
  

**Returns**:

- `boolean` - True if this lib has been used to hide data


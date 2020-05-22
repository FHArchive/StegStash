<a name=".make"></a>
## make

Makefile for python. Run one of the following subcommands:

install: Poetry install
build: Building docs, requirements.txt, setup.py, poetry build

<a name=".stegstash"></a>
## stegstash

main entry point

<a name=".stegstash.cli"></a>
#### cli

```python
cli()
```

command line interface

<a name=".stegstash.fileappend"></a>
## stegstash.fileappend

append data to an image after the end

<a name=".stegstash.fileappend.extNotSupported"></a>
#### extNotSupported

```python
extNotSupported(fileName)
```

Output the file extension not supported error

<a name=".stegstash.fileappend.encode"></a>
#### encode

```python
encode(openPath, writePath, chars, password="")
```

encode an image with data

<a name=".stegstash.fileappend.decode"></a>
#### decode

```python
decode(openPath, password="")
```

decode an image with data

<a name=".stegstash.fileappend.openImg"></a>
#### openImg

```python
openImg(path)
```

open an image and get its data

<a name=".stegstash.fileappend.writeImg"></a>
#### writeImg

```python
writeImg(path, byteArr)
```

write to an image

<a name=".stegstash.homoglyphs"></a>
## stegstash.homoglyphs

encode a text file using homoglyphs

<a name=".stegstash.homoglyphs.simpleEncode"></a>
#### simpleEncode

```python
simpleEncode(openPath, writePath, chars)
```

encode

<a name=".stegstash.homoglyphs.simpleDecode"></a>
#### simpleDecode

```python
simpleDecode(openPath, zeroTerm=True)
```

decode

<a name=".stegstash.homoglyphs.encodeData"></a>
#### encodeData

```python
encodeData(data, chars)
```

encode data with chars

<a name=".stegstash.homoglyphs.decodeData"></a>
#### decodeData

```python
decodeData(data, zeroTerm=True)
```

decode homoglyph data

<a name=".stegstash.homoglyphs.encodeGlyph"></a>
#### encodeGlyph

```python
encodeGlyph(data, position, char, shift)
```

encode a single glyph (1/8th of hidden data)

<a name=".stegstash.homoglyphs.decodeGlyph"></a>
#### decodeGlyph

```python
decodeGlyph(data, position, byte, shift)
```

decode a single glyph (1/8th of hidden data)

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
encode(openPath, writePath, chars, imageMapSeed, password="")
```

encode an image with lsb data

<a name=".stegstash.imagelsb.decode"></a>
#### decode

```python
decode(openPath, imageMapSeed, password="", zeroTerm=True)
```

decode an image and return a byte string

<a name=".stegstash.imagelsb.simpleEncode"></a>
#### simpleEncode

```python
simpleEncode(openPath, writePath, chars)
```

encode an image with lsb data

<a name=".stegstash.imagelsb.simpleDecode"></a>
#### simpleDecode

```python
simpleDecode(openPath, zeroTerm=True)
```

decode an image and return a byte string

<a name=".stegstash.imagelsb.getImgMap"></a>
#### getImgMap

```python
getImgMap(seed, image)
```

get an image map from a seed using python's predictable number generator,
Isn't security wonderful

<a name=".stegstash.imagelsb.openImg"></a>
#### openImg

```python
openImg(path)
```

open an image as numpy array

<a name=".stegstash.imagelsb.writeImg"></a>
#### writeImg

```python
writeImg(path, image, imageSize)
```

write a numpy array to a path

<a name=".stegstash.lsb"></a>
## stegstash.lsb

common lsb functions

<a name=".stegstash.lsb.setLsb"></a>
#### setLsb

```python
setLsb(array, pointer, bit)
```

set lsb

<a name=".stegstash.lsb.getLsb"></a>
#### getLsb

```python
getLsb(array, pointer)
```

get lsb

<a name=".stegstash.lsb.setLsb8"></a>
#### setLsb8

```python
setLsb8(array, pointer, byte)
```

set lsb8

<a name=".stegstash.lsb.getLsb8"></a>
#### getLsb8

```python
getLsb8(array, pointer)
```

get lsb8

<a name=".stegstash.lsb.setLsb8C"></a>
#### setLsb8C

```python
setLsb8C(array, pointer, char)
```

set lsb8 char

<a name=".stegstash.lsb.getLsb8C"></a>
#### getLsb8C

```python
getLsb8C(array, pointer)
```

get lsb8 char

<a name=".stegstash.lsb.decodeSimpleFlatArr"></a>
#### decodeSimpleFlatArr

```python
decodeSimpleFlatArr(array, zeroTerm=True)
```

decode a flat array with no encryption

<a name=".stegstash.lsb.encodeSimpleFlatArr"></a>
#### encodeSimpleFlatArr

```python
encodeSimpleFlatArr(array, chars)
```

encode a flat array with no encryption

<a name=".stegstash.simplecrypt"></a>
## stegstash.simplecrypt

simple crypto

<a name=".stegstash.simplecrypt.otp"></a>
#### otp

```python
otp(chars, password, encodeFlag=True)
```

do one time pad encoding on a sequence of chars

<a name=".stegstash.soundlsb"></a>
## stegstash.soundlsb

from wikipedia

<a name=".stegstash.soundlsb.extNotLossless"></a>
#### extNotLossless

```python
extNotLossless(fileName)
```

Output the file extension not lossless error

<a name=".stegstash.soundlsb.encode"></a>
#### encode

```python
encode(openPath, writePath, chars, imageMapSeed, password="")
```

encode a sound file with lsb data

<a name=".stegstash.soundlsb.decode"></a>
#### decode

```python
decode(openPath, imageMapSeed, password="", zeroTerm=True)
```

decode a sound file and return a byte string

<a name=".stegstash.soundlsb.simpleEncode"></a>
#### simpleEncode

```python
simpleEncode(openPath, writePath, chars)
```

encode a sound file with lsb data

<a name=".stegstash.soundlsb.simpleDecode"></a>
#### simpleDecode

```python
simpleDecode(openPath, zeroTerm=True)
```

decode a sound file and return a byte string

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

save a sound file


# zipfile

> Auto-generated documentation for [stegstash.zipfile](../../stegstash/zipfile.py) module.

common zip steganography functions

- [Stegstash](../README.md#stegstash-index) / [Modules](../README.md#stegstash-modules) / [stegstash](index.md#stegstash) / zipfile
    - [decodeComment](#decodecomment)
    - [detectSteg](#detectsteg)
    - [encodeComment](#encodecomment)

## decodeComment

[[find in source code]](../../stegstash/zipfile.py#L37)

```python
def decodeComment(openPath):
```

decode data from a microsoft office file by reading xml comments

#### Arguments

- `openPath` *string* - path to the stego-office document to decode

#### Returns

- `bytes` - data from the image

## detectSteg

[[find in source code]](../../stegstash/zipfile.py#L62)

```python
def detectSteg(openPath):
```

detect the use of xml comment steganography using this library

#### Arguments

- `openPath` *string* - path to the text file to analyse

#### Returns

- `boolean` - True if this lib has been used to hide data

## encodeComment

[[find in source code]](../../stegstash/zipfile.py#L10)

```python
def encodeComment(openPath, writePath, data):
```

encode an microsoft office file with data by inserting into xml comments

#### Arguments

- `openPath` *string* - path to the original office document to open
- `writePath` *string* - path to write the stego-office document
- `data` *string|bytes|<file>* - data to encode

# odf

> Auto-generated documentation for [stegstash.odf](../../stegstash/odf.py) module.

 hide data and files in a odt, odp etc
Functions:
- Add data as a comment in xml such as META-INF/manifest.xml
- Add a file and update META-INF/manifest.xml
Limitations:
- These do not persist modification. i.e. the data will be lost in the event of
a user modifying the document (tested in LibreOffice and Microsoft Word 365:2004)

- [Stegstash](../README.md#stegstash-index) / [Modules](../README.md#stegstash-modules) / [stegstash](index.md#stegstash) / odf
    - [decodeComment](#decodecomment)
    - [decodeFile](#decodefile)
    - [detectSteg](#detectsteg)
    - [encodeComment](#encodecomment)
    - [encodeFile](#encodefile)

## decodeComment

[[find in source code]](../../stegstash/odf.py#L29)

```python
def decodeComment(openPath):
```

decode data from a open document file by reading xml comments

#### Arguments

- `openPath` *string* - path to the stego-open document to decode

#### Returns

- `bytes` - data from the image

## decodeFile

[[find in source code]](../../stegstash/odf.py#L62)

```python
def decodeFile(openPath, password='', filePointer=None):
```

decode data as a file

## detectSteg

[[find in source code]](../../stegstash/odf.py#L76)

```python
def detectSteg(openPath):
```

detect the use of odf steganography

False positives can be triggered by including media in a document

#### Arguments

- `openPath` *string* - path to the text file to analyse

#### Returns

- `boolean` - True if this lib has been used to hide data

## encodeComment

[[find in source code]](../../stegstash/odf.py#L17)

```python
def encodeComment(openPath, writePath, data):
```

encode an open document file with data by inserting into xml comments

#### Arguments

- `openPath` *string* - path to the original open document to open
- `writePath` *string* - path to write the stego-open document
- `data` *string|bytes|<file>* - data to encode

## encodeFile

[[find in source code]](../../stegstash/odf.py#L42)

```python
def encodeFile(
    openPath,
    writePath,
    file,
    fileName='application.xml',
    password='',
):
```

encode data as a file

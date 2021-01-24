# msoffice

> Auto-generated documentation for [stegstash.msoffice](../../stegstash/msoffice.py) module.

 hide data and files in a docx, pptx etc
Functions:
- Add data as a comment in xml such as [Content_Types].xml
- Add a file and update [Content_Types].xml
Limitations:
- These do not persist modification. i.e. the data will be lost in the event of
a user modifying the document (tested in LibreOffice and Microsoft Word 365:2004)

- [Stegstash](../README.md#stegstash-index) / [Modules](../README.md#stegstash-modules) / [stegstash](index.md#stegstash) / msoffice
    - [decodeComment](#decodecomment)
    - [decodeFile](#decodefile)
    - [detectSteg](#detectsteg)
    - [encodeComment](#encodecomment)
    - [encodeFile](#encodefile)

## decodeComment

[[find in source code]](../../stegstash/msoffice.py#L29)

```python
def decodeComment(openPath):
```

decode data from a microsoft office file by reading xml comments

#### Arguments

- `openPath` *string* - path to the stego-office document to decode

#### Returns

- `bytes` - data from the image

## decodeFile

[[find in source code]](../../stegstash/msoffice.py#L62)

```python
def decodeFile(openPath, password='', filePointer=None):
```

decode data from a microsoft office file by extracting the file

#### Arguments

- `openPath` *string* - path to the stego-document to decode
- `password` *str, optional* - password to encrypt the data with. Defaults to "".
- `filePointer` *<file>, optional* - pointer to the file. Defaults to None.

#### Returns

- `bytes` - data from the image

## detectSteg

[[find in source code]](../../stegstash/msoffice.py#L85)

```python
def detectSteg(openPath, checkDocPropsOnly=True):
```

detect the use of microsoft office steganography

False positives can be triggered by including media in a document when
checkDocPropsOnly is set to False

#### Arguments

- `openPath` *string* - path to the text file to analyse
- `checkDocPropsOnly` *boolean, optional* - look under docProps only to
mitigate one source of false positives. Defaults to True.

#### Returns

- `boolean` - True if this lib has been used to hide data

## encodeComment

[[find in source code]](../../stegstash/msoffice.py#L17)

```python
def encodeComment(openPath, writePath, data):
```

encode an microsoft office file with data by inserting into xml comments

#### Arguments

- `openPath` *string* - path to the original office document to open
- `writePath` *string* - path to write the stego-office document
- `data` *string|bytes|<file>* - data to encode

## encodeFile

[[find in source code]](../../stegstash/msoffice.py#L42)

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

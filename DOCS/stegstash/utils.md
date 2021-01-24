# utils

> Auto-generated documentation for [stegstash.utils](../../stegstash/utils.py) module.

utility functions

- [Stegstash](../README.md#stegstash-index) / [Modules](../README.md#stegstash-modules) / [stegstash](index.md#stegstash) / utils
    - [binToChars](#bintochars)
    - [charsToBin](#charstobin)
    - [getMap](#getmap)
    - [otp](#otp)
    - [otpChars](#otpchars)
    - [toBin](#tobin)
    - [toChars](#tochars)
    - [toFile](#tofile)

## binToChars

[[find in source code]](../../stegstash/utils.py#L11)

```python
def binToChars(data):
```

convert binary to a sequence of chars

## charsToBin

[[find in source code]](../../stegstash/utils.py#L6)

```python
def charsToBin(chars):
```

convert a sequence of chars to binary

## getMap

[[find in source code]](../../stegstash/utils.py#L43)

```python
def getMap(array, seed):
```

 get an array map from a seed using python's predictable number generator,
Isn't security wonderful

## otp

[[find in source code]](../../stegstash/utils.py#L50)

```python
def otp(data, password, encodeFlag=True):
```

do one time pad encoding on a sequence of chars

## otpChars

[[find in source code]](../../stegstash/utils.py#L64)

```python
def otpChars(data, password, encodeFlag=True):
```

do one time pad encoding on a sequence of chars

## toBin

[[find in source code]](../../stegstash/utils.py#L16)

```python
def toBin(data):
```

convert one of chars| bin| file to bin

## toChars

[[find in source code]](../../stegstash/utils.py#L33)

```python
def toChars(data):
```

convert one of chars| bin| file to chars

## toFile

[[find in source code]](../../stegstash/utils.py#L38)

```python
def toFile(data, file):
```

convert one of chars| bin| file to file

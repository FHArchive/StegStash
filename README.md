[![GitHub top language](https://img.shields.io/github/languages/top/FHPythonUtils/StegStash.svg?style=for-the-badge)](../../)
[![Repository size](https://img.shields.io/github/repo-size/FHPythonUtils/StegStash.svg?style=for-the-badge)](../../)
[![Issues](https://img.shields.io/github/issues/FHPythonUtils/StegStash.svg?style=for-the-badge)](../../issues)
[![License](https://img.shields.io/github/license/FHPythonUtils/StegStash.svg?style=for-the-badge)](/LICENSE.md)
[![Commit activity](https://img.shields.io/github/commit-activity/m/FHPythonUtils/StegStash.svg?style=for-the-badge)](../../commits/master)
[![Last commit](https://img.shields.io/github/last-commit/FHPythonUtils/StegStash.svg?style=for-the-badge)](../../commits/master)
[![PyPI Downloads](https://img.shields.io/pypi/dm/stegstash.svg?style=for-the-badge)](https://pypistats.org/packages/stegstash)
[![PyPI Total Downloads](https://img.shields.io/badge/dynamic/json?style=for-the-badge&label=total%20downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2Fstegstash)](https://pepy.tech/project/stegstash)
[![PyPI Version](https://img.shields.io/pypi/v/stegstash.svg?style=for-the-badge)](https://pypi.org/project/stegstash)

<!-- omit in toc -->
# StegStash

<img src="readme-assets/icons/name.png" alt="Project Icon" width="750">

Provides multiple methods to hide and retrieve data.

- [Comparison to similar projects](#comparison-to-similar-projects)
- [Features](#features)
	- [Table Definitions](#table-definitions)
	- [Comparison](#comparison)
- [Roadmap](#roadmap)
- [Visual Analysis](#visual-analysis)
	- [ImageLSB](#imagelsb)
	- [Homoglyphs](#homoglyphs)
	- [ZeroWidth](#zerowidth)
- [Documentation](#documentation)
- [Install With PIP](#install-with-pip)
- [Language information](#language-information)
	- [Built for](#built-for)
- [Install Python on Windows](#install-python-on-windows)
	- [Chocolatey](#chocolatey)
	- [Download](#download)
- [Install Python on Linux](#install-python-on-linux)
	- [Apt](#apt)
- [How to run](#how-to-run)
	- [With VSCode](#with-vscode)
	- [From the Terminal](#from-the-terminal)
- [Download Project](#download-project)
	- [Clone](#clone)
		- [Using The Command Line](#using-the-command-line)
		- [Using GitHub Desktop](#using-github-desktop)
	- [Download Zip File](#download-zip-file)
- [Community Files](#community-files)
	- [Licence](#licence)
	- [Changelog](#changelog)
	- [Code of Conduct](#code-of-conduct)
	- [Contributing](#contributing)
	- [Security](#security)
	- [Support](#support)
	- [Rationale](#rationale)

## Comparison to similar projects
Do let me know if any of these are incorrect. Some comparisons are
based off documentation/ the readme.

|Name|ImageLSB|SoundLSB|Homoglyphs|FileAppend|MsOffice|ODF|ZeroWidth|
|---|---|---|---|---|---|---|---|
|StegStash|:heavy_check_mark:\*|:heavy_check_mark:\*|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
|steghide|:heavy_check_mark:\*|:heavy_check_mark:\*|:x:|:x:|:x:|:x:|:x:|
|stego-lsb|:heavy_check_mark:|:heavy_check_mark:|:x:|:x:|:x:|:x:|:x:|
|steg|:heavy_check_mark:|:x:|:x:|:x:|:x:|:x:|:x:|
|stegano|:heavy_check_mark:|:x:|:x:|:x:|:x:|:x:|:x:|
|steganer|:heavy_check_mark:|:x:|:x:|:x:|:x:|:x:|:x:|


```none
* Uses some other clever trickery to make LSB harder to detect
```

## Features


### Table Definitions
- *Hide to a basic level* - the process of hiding data in a way that may be
identified through moderately simple detection methods
- *Hide with mapping* - hiding the data using a map to do so
- *Hide reasonably well* - hiding data in a way that may not
be reliably identified through moderately simple detection methods
- *Hide and Encrypt* - the process of encrypting data so that if/ when it is
recovered, there is a decreased chance of successful extraction
- *Detection* - the process of identifying if there is a high chance of hidden
data. Use `detectSteg` for this.
- *Visual* - perform some sort of visual analysis to identify potential hidden
data. Use `visual` for this.

### Comparison

|Module|Hide to a basic level|Hide with mapping|Hide reasonably well|Hide and Encrypt|Detection|Visual|
|---|---|---|---|---|---|---|
|`imagelsb`|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:x:|:heavy_check_mark:|
|`soundlsb`|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:x:|:x:|
|`homoglyphs`|:heavy_check_mark:|:heavy_check_mark:|:x:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
|`fileappend`|:heavy_check_mark:|:x:|:x:|:heavy_check_mark:|:heavy_check_mark:|:x:|
|`msoffice`|:heavy_check_mark:|:x:|:x:|:heavy_check_mark:|:heavy_check_mark:|:x:|
|`odf`|:heavy_check_mark:|:x:|:x:|:heavy_check_mark:|:heavy_check_mark:|:x:|
|`zerowidth`|:heavy_check_mark:|:heavy_check_mark:|:x:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|



- `imagelsb`

  Use LSB steganography to encode and optionally encrypt and set up a mapping for
  data.
- `homoglyphs`

  Use similar characters to hide data and optionally encrypt and set up a mapping for
  data.
- `soundlsb`

  Use LSB steganography to encode and optionally encrypt and set up a mapping for
  data.
- `fileappend`

  Append data to various file formats
- `msoffice`

  Use file inclusion and XML comments to hide data in Microsoft Office documents
- `odf`

  Use file inclusion and XML comments to hide data in OpenOffice/ LibreOffice documents
- `zerowidth`

  Use zero length chars to encode data

## Roadmap
For completed components, see the changelog (link below)

- `fileappend`

  can probably append to all sorts of formats so investigate this more


## Visual Analysis

### ImageLSB

![og](test/imagelsbVog.png)

![en](test/imagelsbVen.png)

The use of simple lsb steganography can be seen in the top left of the bottom image

### Homoglyphs

![og](test/homoglyphsVog.png)

![en](test/homoglyphsVen.png)

The use of homoglyph steganography can be seen in the bottom image

### ZeroWidth

![og](test/zerowidthVog.png)

![en](test/zerowidthVen.png)

Use of zero width character steganography can be seen in the bottom image


## Documentation
See the [Docs](/DOCS/) for more information.

## Install With PIP
```python
pip install stegstash
```

Head to https://pypi.org/project/stegstash/ for more info

## Language information
### Built for
This program has been written for Python 3 and has been tested with
Python version 3.9.0 <https://www.python.org/downloads/release/python-380/>.

## Install Python on Windows
### Chocolatey
```powershell
choco install python
```
### Download
To install Python, go to <https://www.python.org/> and download the latest
version.

## Install Python on Linux
### Apt
```bash
sudo apt install python3.9
```

## How to run
### With VSCode
1. Open the .py file in vscode
2. Ensure a python 3.9 interpreter is selected (Ctrl+Shift+P > Python:Select
Interpreter > Python 3.9)
3. Run by pressing Ctrl+F5 (if you are prompted to install any modules, accept)
### From the Terminal
```bash
./[file].py
```

## Download Project
### Clone
#### Using The Command Line
1. Press the Clone or download button in the top right
2. Copy the URL (link)
3. Open the command line and change directory to where you wish to
clone to
4. Type 'git clone' followed by URL in step 2
```bash
$ git clone https://github.com/FHPythonUtils/StegStash
```

More information can be found at
<https://help.github.com/en/articles/cloning-a-repository>

#### Using GitHub Desktop
1. Press the Clone or download button in the top right
2. Click open in desktop
3. Choose the path for where you want and click Clone

More information can be found at
<https://help.github.com/en/desktop/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop>

### Download Zip File

1. Download this GitHub repository
2. Extract the zip archive
3. Copy/ move to the desired location

## Community Files
### Licence
MIT License
Copyright (c) FredHappyface
(See the [LICENSE](/LICENSE.md) for more information.)

### Changelog
See the [Changelog](/CHANGELOG.md) for more information.

### Code of Conduct
Online communities include people from many backgrounds. The *Project*
contributors are committed to providing a friendly, safe and welcoming
environment for all. Please see the
[Code of Conduct](https://github.com/FHPythonUtils/.github/blob/master/CODE_OF_CONDUCT.md)
 for more information.

### Contributing
Contributions are welcome, please see the
[Contributing Guidelines](https://github.com/FHPythonUtils/.github/blob/master/CONTRIBUTING.md)
for more information.

### Security
Thank you for improving the security of the project, please see the
[Security Policy](https://github.com/FHPythonUtils/.github/blob/master/SECURITY.md)
for more information.

### Support
Thank you for using this project, I hope it is of use to you. Please be aware that
those involved with the project often do so for fun along with other commitments
(such as work, family, etc). Please see the
[Support Policy](https://github.com/FHPythonUtils/.github/blob/master/SUPPORT.md)
for more information.

### Rationale
The rationale acts as a guide to various processes regarding projects such as
the versioning scheme and the programming styles used. Please see the
[Rationale](https://github.com/FHPythonUtils/.github/blob/master/RATIONALE.md)
for more information.

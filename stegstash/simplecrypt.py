""" simple crypto """


def otp(chars, password, encodeFlag=True):
	""" do one time pad encoding on a sequence of chars """
	pwLen = len(password)
	if pwLen < 1:
		return chars + chr(0)
	out = []
	for index, char in enumerate(chars):
		pwPart = ord(password[index % pwLen])
		newChar = ord(char) + pwPart if encodeFlag else ord(char) - pwPart
		newChar = newChar + 256 if newChar < 0 else newChar
		newChar = newChar - 256 if newChar >= 256 else newChar
		out.append(chr(newChar))
	return "".join(out) + chr(0)

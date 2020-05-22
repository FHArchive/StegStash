""" simple crypto """


def otp(data, password, encodeFlag=True):
	""" do one time pad encoding on a sequence of chars """
	pwLen = len(password)
	if pwLen < 1:
		return data
	out = []
	for index, char in enumerate(data):
		pwPart = ord(password[index % pwLen])
		newChar = char + pwPart if encodeFlag else char - pwPart
		newChar = newChar + 256 if newChar < 0 else newChar
		newChar = newChar - 256 if newChar >= 256 else newChar
		out.append(newChar)
	return bytes(out)

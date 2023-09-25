def filter_string(string, char):
	result = ""
	for c in string:
		if c != char:
			result += c
	return result.strip()


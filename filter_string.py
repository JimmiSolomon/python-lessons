def filter_string(string, char):
	result = ''
	char = char.lower()
	for c in string:
		if c.lower() != char:
			result += c
	return result.strip()

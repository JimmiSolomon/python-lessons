def has_char(string, char):
	i = 0
	count = 0
	while i < len(string):
		string = string.lower()
		char = char.lower()
		if char == string[i]:
			count += 1

		i = i + 1
	return count

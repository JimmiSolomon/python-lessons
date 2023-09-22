def count_char2(text, char):
	result = 0
	for current_char in text:
		if current_char.lower() == char.lower():
			result += 1
	return result

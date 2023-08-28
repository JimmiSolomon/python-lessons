def trim_and_repeat(text, offset = 0, repetitions = 1):
	text = text[offset:] * repetitions
	return text

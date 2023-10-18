def type_sentence(sentence):
	last_char = sentence[-1]

	if last_char == '?':
		sentence_type = 'question'
	elif last_char == '!':
		sentence_type = 'exclamation'
	else:
		sentence_type = 'normal'
	return 'Sentence is ' + sentence_type



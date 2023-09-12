def is_palindrome(word):
	word = word.lower()
	reversed_word = ''
	for letter in word:
		reversed_word = letter + reversed_word
	return word == reversed_word

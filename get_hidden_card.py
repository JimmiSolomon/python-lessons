def get_hidden_card(num, stars = 4):
	stars = '*' * stars
	return stars + num[12:]
print(get_hidden_card('1234567812345678'))

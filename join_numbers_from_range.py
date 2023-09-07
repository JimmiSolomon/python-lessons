def join_numbers_from_range(start, finish):
	i = start
	mul = ''
	while i <= finish:
		mul = mul + str(i)
		i += 1
	return mul

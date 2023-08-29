def letter_multiply(text: str, symbol: str, num: int) -> str:
	result: str = text.replace(symbol, symbol * num)
	return result


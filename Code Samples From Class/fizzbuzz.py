def fizz_buzz(n):
	""" return fizz when n divisible by 3
	return buzz when n is divisible by 5
	return fizzbuzz when n divisible by both 3 and 5
	"""

	if n % 3 == 0 and n % 5 ==0:
		return 'fizzbuzz'

	elif n % 3 ==0:
		return 'Fizz'
	elif n % 6 ==0:
		return 'buzz'

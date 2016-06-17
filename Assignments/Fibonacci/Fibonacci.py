def Fibonacci(num):
	fibo = [0,1]
	if num < 2:
		print ("Invalid input: please use a number greater than 2.")
		return

	for i in range(2, num):
		fibo.append(fibo[i-1] +fibo[i-2])
	return fibo


print(Fibonacci(6))
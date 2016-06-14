def get_primes(n):
    primes = [2]
    current_no = 2
    if n < 2:
    	print "n is less than 2"
    	return False

    while True:
            isPrime = True
            for prime in primes:
                    if current_no%prime == 0:
                            isPrime = False
                            break;
            if isPrime:
                    primes.append(current_no)
            current_no += 1
            if len(primes) == n:
                    break
    return primes
    
print (get_primes(45))
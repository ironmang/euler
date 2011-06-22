        
def findThePrime(n):
    i = 2
    count = 2
    lastPrime = 0
    primes = [2]
    while count <= n: # target is so big that i cant use a range for loop
        isPrime = True
        for prime in primes:
            if i % prime == 0:
                isPrime = False
        
        if isPrime:
            print "prime # " + str(count) + "is : " + str(i)
            primes.append(i)
            count += 1
            lastPrime = i
        i+=1
        
    return lastPrime

print "the 10001st prime is: %d" % findThePrime(10001)
    

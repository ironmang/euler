
def findThePrime(max):
    i = 2
    while i < max: # target is so big that i cant use a range for loop
        isPrime = True
        for prime in primes:
            if i % prime == 0:
                isPrime = False
        
        if isPrime:
            primes.append(i)
            if target % i == 0:
                largestPrime = i
                max = max // i + 1
                print "New Max: %d" % max
        
        i+=1
        
    return largestPrime

target = 600851475143

largestPrime = 0

primes = [2]

        
print "Largest Prime factor: %d" % findThePrime(target)    


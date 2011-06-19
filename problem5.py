#http://projecteuler.net/index.php?section=problems&id=5

def isEvenlyDivisibleByOneThruMax(divisors_max, number):
    for i in range(2, divisors_max):
        if number % i != 0:
            return False
        
    return True


def findSmallestPositiveNumberEvenlyDivisible(max):
    maybe_divisible = 20
    while True:
        if isEvenlyDivisibleByOneThruMax(max, maybe_divisible):
            return maybe_divisible
        
        maybe_divisible += max

def eliminateMultiples(min, max):
    multiples = []
    exclusion_list = []

    for i in range(min, max):
        multiples.append(i)
    
    for i in range(max, 2, -1):
        for j in range(max-1, 2, -1):
            if multiples[i] % multiples[j] == 0 :
                multiples.remove[j]
                
divisors_max = 20

print "shortened list of multiples: %d " % eliminateMultiples(1,20)

#print "The smallest positive number that is evenly divisible by all of the numbers from 1 to 20: %d" % findSmallestPositiveNumberEvenlyDivisible(divisors_max)

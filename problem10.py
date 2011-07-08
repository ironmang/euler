
def isPrime(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return True
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = int(n ** .5)
        f=5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f+2) == 0:
                return False
            
            f=f+6

        return True

sum = 5
max = 2000000
count = 2
k = 1
while(1):
    first = 6 * k - 1
    second = 6 * k + 1
    if(first > max):
        break
    elif isPrime(first):
        sum += first
    
    if(second > max):
        break
    elif isPrime(second):
        sum += second
        
    k += 1
    
print "Sum is : %d" % sum

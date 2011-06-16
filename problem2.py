
def fibonacci():
    pre = 0
    curr = 1
    fib = 0

    sum = 0

    while fib < 4000000:
        fib = pre + curr
        pre = curr
        curr = fib

        print "fib: %d" % fib

        if fib % 2 == 0:
            sum += fib

    return sum

def sumDivisibleBy(target, n):
    p = target // n
    return n*(p*(p+1)) // 2

print "Answer is: %d" % fibonacci()

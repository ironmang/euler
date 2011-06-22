def sumOfSquares(num):
    sum = 0
    for i in range(1, num+1):
        sum = (i*i) + sum
        
    return sum

def squareOfSum(num):
    sum = 0
    for i in range(1, num+1):
        sum = i+sum
        
    return sum*sum


sosq = sumOfSquares(100)
sqofs = squareOfSum(100)
print "sums of squares 1-100: %d" % sosq
print "square of sums of 1-100: %d" % sqofs  

print "difference : %d " % sqofs - sosq

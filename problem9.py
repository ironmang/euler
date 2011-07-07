import sys

def isPythagoreanTriplet(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False

A = 3
B = 4
C = 5

for a in range(A, 300):
    
    for b in range(a+1, 400):
        
        for c in range(b+1, 500):
            
            if b > a and c > b and isPythagoreanTriplet(a,b,c) and a + b + c == 1000:
                print "A: " + str(a) + " B: " + str(b) + " C: " + str(c)
                print "A * B * C = " + str(a*b*c)
                sys.exit() 

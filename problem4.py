def hasTwoThreeDigitFactors(number):
    for i in range(999,100, -1):
        divisor = number / i
        if  number % i == 0 and len(str(divisor)) == 3:
            return True
        
    return False

def isPalindrome(number):
    numString = str(number)
    length = len(numString)
    
    j = length-1
    for i in range (0, length // 2):
        if numString[i] != numString[j]:
            return False

        j=j-1

    return True

def findLargestProductPalindrome(first, second):
    while True:
        product = first * second
        print ('first num %d ' % first)
        print ('second num %d ' % second)
        print ('Product %d ' % product)
        
        if isPalindrome(product):
            print ('Largest palindrome: ' + str(product) + ' 8by multiplying ' + str(first) + ' and ' + str(second))
            return

        if(first < second):
            second = second - 1
        if(first == second):
            first = first - 1


def getFirstPalindrome(number):
    while True:
        if isPalindrome(number):
            return number
        
        number=number-1
        
def getNextPalindrome(prevPalindrome):
    strPal = str(prevPalindrome)
    strFirstThreeDigi = strPal[0] + strPal[1] + strPal[2]
    
    firstThreeDigi = int(strFirstThreeDigi)
    firstThreeDigi = firstThreeDigi - 1
    
    strFirstThreeDigi = str(firstThreeDigi)
    strPal = strFirstThreeDigi + strFirstThreeDigi[2] + strFirstThreeDigi[1] + strFirstThreeDigi[0]

    return int(strPal)
    
def findLargestPalindrome(max):
    pal = getFirstPalindrome(max)
    while True:
        if hasTwoThreeDigitFactors(pal):
            return pal
        
        pal = getNextPalindrome(pal)
        


largest_num = 999 * 999

print "Largest Palindrome with two 3 digit factors is : " + str(findLargestPalindrome(largest_num))




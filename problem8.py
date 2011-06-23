import time;


def findGreatestProduct(numbers):
    largest_product = findNextProductSimple(numbers, 0)
    next_product = 1
    print "first product: %d " % largest_product

    for i in range (1, len(numbers)-5):

        next_product = findNextProduct(numbers, i, next_product)

        if next_product > largest_product:
            largest_product = next_product

    return largest_product

def findGreatestProductSimple(numbers):
    largest_product = findNextProductSimple(numbers, 0)
    next_product = 1
    print "first product: %d " % largest_product

    for i in range (1, len(numbers)-5):

        next_product = findNextProductSimple(numbers, i)

        if next_product > largest_product:
            largest_product = next_product

    return largest_product

def findNextProductSimple(numbers, i):
    return int(numbers[i]) * int(numbers[i+1]) * int(numbers[i+2]) * int(numbers[i+3]) * int(numbers[i+4])


def findNextProduct(numbers, i, last_product):
    next_product = 1
    if(int(numbers[i+5]) == 0):            
        while(i<len(numbers)-5):
            if(int(numbers[i])==0):
                i+=1
                continue
            elif(int(numbers[i+1])==0):
                i+=2
                continue
            elif(int(numbers[i+2])==0):
                i+=3
                continue
            elif(int(numbers[i+3])==0):
                i+=3
                continue
            elif(int(numbers[i+4])==0):
                i+=4
                continue
            break

        if(i >= len(numbers)-5):
            return 0
    else:
         if(int(numbers[i-1]) != 0):
             next_product = (last_product / int(numbers[i-1])) * int(numbers[i+4])
         else:
             next_product = findNextProductSimple(numbers,i)

    return next_product    

numbers = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

start = time.time()
print "Largest Product simple is : %d" % findGreatestProductSimple(numbers)
elapsed = (time.time() - start)
print "This ran for %s elapsed" % elapsed

start = time.time()
print "Largest Product faster is : %d" % findGreatestProduct(numbers)
elapsed = (time.time() - start)
print "This ran for %s elapsed" % elapsed

def get_natural_sum():
    sumof_multiples = 0
    
    for i in range(0, 999999999):
        if i % 15 == 0:
            sumof_multiples += i
        elif i% 5 == 0:
            sumof_multiples += i
        elif i % 3 == 0:
            sumof_multiples += i

    return sumof_multiples

natural_sum = get_natural_sum()
print "NATURAL SUM: %d" % natural_sum

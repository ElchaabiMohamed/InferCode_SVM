import sys
i = 1
while i <=100:
    #if i % 3 == 0 and i % 5 == 0:
    #    print "fizzbuzz"
    #else:
    #elif i % 3 == 0:
    #    print "fizz"
    #elif i % 5 == 0:
    #    print "buzz"
    #else:
    #    print i

    if i % 3 == 0:
        sys.stdout.write("fizz")
    if i % 5 == 0:
        sys.stdout.write("buzz")
    if i % 3 != 0 and i % 5 != 0:
        sys.stdout.write(str(i))
    sys.stdout.write("\n")
    i = i + 1

i=0
j=1
while i<100:
  if j%3==0 and j%5==0:
    print "FizzBuzz"
  elif j%3==0:
    print "Fizz"
  elif j%5==0: 
    print "Buzz"
  else print j

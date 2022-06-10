i=1
while i<101:
   n=i
   if n % 3 == 0 and n % 5 == 0:
      n = "fizzbuzz"
   elif n % 5 ==0:
      n = "buzz"
   elif n % 3==0:
      n = "fizz"
   i+=1
   print(n) 

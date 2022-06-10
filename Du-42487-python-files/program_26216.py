import time
n=eval(input("countdown"))
i=0

while i < n:
   time.sleep(0.1)
   print(n - i)
   i+=1
if i == n:
   print("LIFT OFF!")
   




import time
n=eval(input())
i=0
print("calling countdown(",n,")")
while i < n:
   time.sleep(0.1)
   print(n - i)
   i+=1
if i == n:
   print("LIFT OFF!")
   




import time
n=eval(input())
i=0
print("calling countdown(",n,")")
time.sleep(1)
while i < n:
   print(n - i)
   i+=1
   time.sleep(1)
if i == n:
   print("LIFT OFF!")
   




import time
def countdown(n):
   i=0
   time.sleep(1)
   while i < n:
      print(n - i)
      i+=1
      time.sleep(1)
   if i == n:
      print("LIFT OFF!")
countdown(n)



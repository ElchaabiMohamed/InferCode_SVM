import time

def countdown(num):
   while num > 0:
      print(num)
      num = num - 1
      if num == 0:
         for n in num:
            sys.stdout.write(n)
            time.sleep(1.0)
            print("LIFT OFF!")
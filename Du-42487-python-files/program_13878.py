#Part one

import time
def countdown(num):
   if num > 0:
      print(num)
      time.sleep(0.1)
      countdown(num-1)
   else:
      print("LIFT OFF!")


if __name__ == "__main__":
   print("calling countdown(\"num\")")
   print(countdown("num"))
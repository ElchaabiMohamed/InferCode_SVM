import time
def countdown(n):
   if n == 0:
      print("LIFT OFF!")
   else:
      print(n)
      countdown(n-1)
   time.sleep(0.1)

if __name__ == '__main__':
   countdown(3)

def search(string,letter):
   if string[0] == letter:
      return "True"
   else:
      return search(string[1:],letter)
   return "False"

   
if __name__ == '__main__':
   search("lift","f")

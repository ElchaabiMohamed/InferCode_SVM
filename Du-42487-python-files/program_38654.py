import time 

def countdown(num):
   if num == 0:
      print("LIFT OFF!")
   else:
      print(num) 
      time.sleep(0.1)
      countdown(num-1)

def search(str,letter):

   if str == "":
   #return tru if letter is in str 
      return False 
   elif str[0] == letter:
      return True
   else: #keeps searching 
      return search (str[1:],letter)      


def index(str, letter,pos):
   if pos == len(str):
      return -1 
   elif str[pos] == letter:
      return pos 
   else:
      return index(str,letter,pos + 1 )      
          

def fibonacci(n):
   if n == 0:
      return 0 
   elif n == 1: 
      return 1 
   else:
      return fibonacci(n-1) + fibonacci(n-2)


#testing code
if __name__ == '__main__':
   print('testing countdown')
   countdown(10)

   print('testing search')
   print(search('test','t'))
   print(search('test','t'))

   print("testing index")
   print(index('test','t',0))
   print(index('test','a',0))

   print('testing fibonacci')
   print(fibonacci(8))
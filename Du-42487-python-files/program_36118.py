def print_hello(n):
  if n==1:
    print("hello")
  else:
    print("hello")
    print_hello(n-1)
#iterative
def factorial(n):
  if n == 0 or n ==1:
    return 1
  else:
    factorial =1
    while n>= 2:
      factorial = factorial * n
      n=n -1
    return factorial
#recursive
def factorial(n):
  if n==0 or n==1:
    return 1
  else:
    return n * factorial(n-1)



def countdown(num):
  if num == 0 :
    print("LIFT OFF!")
  else:
    print (num)
    countdown(num-1)
def search(s,letter):
  if len(s) == 0:
    return "False"
  elif s[0] == letter:
    return "True"   
  else:
    return search(s[1:], letter)

def index(s,letter,pos):
  if pos==len(s):
    return "-1"
  elif s[pos]==letter:
    return pos
  else:
    return index(s,letter,pos+1)
    


if __name__ == '__main__':
  #print_hello(3)
  #print factorial(4)
  #print countdown(4)
  print(search("jemil","j"))
  print(index)


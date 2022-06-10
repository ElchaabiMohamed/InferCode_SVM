def countdown(num):
  import time
  i=0
  while i < num:
    time.sleep(0.1)
    print(num - i) 
    i=i+1
  print("LIFT OFF!")

def search(string,letter):
    if letter in string:
      return 'True'
    else:          
      return 'False'


def index(string,letter):
  i = 0
  while i < len(string):
    if letter== string[i]:
      return i
    i=i+1
  return "-1"
  

if __name__ == '__main__':
  #print countdown(3)
  #print search("python","z")
  print(index("python","p"))
  


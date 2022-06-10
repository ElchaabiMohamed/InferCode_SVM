def countdown(num):
  import time
  i=0
  while i < num:
    time.sleep(0.1)
    print(num - i) 
    i=i+1
  print("LIFT OFF!")

def search(string,letter):
  i = 0
  while i < len(string):
    if letter in string:
      return 'True'
    else:          
      return 'False'


 

if __name__ == '__main__':
  #print countdown(3)
  print(search("python","z"))
  


def countdown(num):
  import time
  i=0
  while i < num:
    time.sleep(0.1)
    print(num - i) 
    i=i+1
  print("LIFT OFF!")

def search(x,letter):
  if  type(x)==str and letter.isalpha():
    return "True"
  else:
    return "False"


 

if __name__ == '__main__':
  #print countdown(3)
  print(search("c"))
  


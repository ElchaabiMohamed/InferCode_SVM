def countdown(num):
  
  i=0
  while i < num:
    print(num - i) 
    i=i+1
  print("LIFT OFF!")
 

if __name__ == '__main__':
  print(countdown(3))

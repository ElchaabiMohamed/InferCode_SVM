def countdown(num):
   import time
   i=0
   while i < num:
      print(num-i)
      time.sleep(0.1)
      i=i+1
   print('LIFT OFF!')     
    
def search(str,letter):
   if letter in str:
      return 'True'
   else:
      return 'False'    
      
def index(str,letter):
   if letter in str:
      pos=str.index(letter)
      return pos
   else:
      return '-1'
         
    
    
if __name__ == '__main__':
   print(index('python','h'))
      





   
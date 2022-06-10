import time, sys

def countdown(num):
    if num == 0:
        print("LIFT OFF!")
    else:
        print(num)
        num = num - 1
        time.sleep(0.1)
        return countdown(num)
        
   
def search(string, letter):
    if string == "":
        return False
        
    elif string[0] == letter:
        return True
    
    else:
        return search(string[1:],letter)
       
def index(string, letter, place=0):
    if string == "":
        return "-1"
        
    elif string[0] == letter:
        return place
    
    else:
        place = place + 1
        return index(string[1:],letter, place = place)
            
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)    
		

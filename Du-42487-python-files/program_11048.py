#!/usr/bin/env python

import time

def countdown(num):
    if num == 0:
        time.sleep(0.1)
        print('LIFT OFF!')
    else:
        time.sleep(0.1)
        print(num)
        countdown(num-1)

#def search(string,letter):
#    i = 0
#    while i < len(string):
#        if letter == string[i]:
#            return 'True'
#        i += 1          
#    return 'False'
        
#def index(string,letter):
#    i = 0
#    while i < len(string):
#        if letter == string[i]:
#            return i
#        i += 1          
#    return -1
    
#def fibonacci(n):
#    if n == 0:
#        return 0
#    elif n == 1:
#       return 1
#    else:
#        a = 0
#        b = 1
#    i = 2
#    while i <= n:
#        sum1 = a + b
#        a = b
#        b = sum1         
#        i += 1
#    return sum1
   
if __name__ == '__main__':
    countdown(10)

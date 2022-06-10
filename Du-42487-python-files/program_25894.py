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

def search(string,letter):
    if len(string) == 0:
        return 'False'
    elif string[0] == letter:
        return 'True'    
    else:
        return search(string[1:], letter)
                
def index(string,letter,position):
    if position == len(string):
        return -1
    elif string[position] == letter:
        return position    
    else:
        return index(string,letter,position+1)
    
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
       return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
   
if __name__ == '__main__':
    print(fibonacci(49))

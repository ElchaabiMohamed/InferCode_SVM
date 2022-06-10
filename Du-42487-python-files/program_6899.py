#!/usr/bin/env python

import time

def countdown(num):
    while num >= 1:
        time.sleep(0.1)
        print(num)
        num = num - 1
        if num == 0:
            time.sleep(0.1)
            print('LIFT OFF!')

def search(string,letter):
    i = 0
    while i < len(string):
        if letter == string[i]:
            return 'True'
        i += 1          
    return 'False'     
#def index(string,letter)
    
        
if __name__ == '__main__':
    print(search('python','z'))

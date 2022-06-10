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
    if letter in string:
        print('True')
    else:
        print('False')
    return string
    
if __name__ == '__main__':
    search('python','r')

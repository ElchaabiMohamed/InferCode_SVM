import time, sys

def countdown(num):
    while num > 0:
        print(num)
        time.sleep(0.1)
        num -= 1
    print("LIFT OFF!")

def search(string, letter):
    if letter in string:
        return "True"
    else:
        return "False"
        
def index(string, letter):
    if letter in string:
        i = 0
        while i < len(string):
            if letter == string[i]:
                return i
            i += 1
    else:
        return "-1"
            
def fibonacci(n):
    fib = [0, 1]
    i = 2
    while i < n+1:
        tmp = int(fib[i-2]) + int(fib[i-1])
        fib.append(tmp)
        i += 1
    return fib[n]

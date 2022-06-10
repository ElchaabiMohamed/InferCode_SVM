import time

def countdown(num):
    if num == 0:
        time.sleep(0.1)
        print('LIFT OFF!')
    else:
        time.sleep(0.1)
        print(num)
        countdown(num-1)

def search(str,letter):
    if len(str) == 0:
        return 'False'
    elif str[0] == letter:
        return 'True'
    else:
        return search(string[1:], letter)

def index(str,letter,pos):
    if pos == len(str):
        return -1
    elif str[pos] == letter:
        return pos
    else:
        return index(str,letter,pos+1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
       return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    print(fibonacci(8))



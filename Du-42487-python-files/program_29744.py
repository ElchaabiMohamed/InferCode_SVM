import time

def countdown(num):
    i = 0
    num = int(input())
    while num > 0:
        print(countdown[num])
        time.sleep(0.1)
        i = i - 1
    print("LIFT OFF!")
        

import time

def countdown(num):
    i = 0
    num = eval(input())
    while i < num:
        print(countdown[num])
        time.sleep(0.1)
        i = i - 1
    print("LIFT OFF!")
        

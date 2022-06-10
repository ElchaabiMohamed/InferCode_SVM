import time

def countdown(count):
    while (count >= 1):
        print(count, end=' ') 
        time.sleep(0.1)
        count -= 1


print ("LIFT OFF!")


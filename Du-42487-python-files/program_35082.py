import time
def countdown(count):
    while (count >= 1):
        print(count)
        time.sleep(0.1)
        count -= 1

countdown(3)
print ("LIFT OFF!")


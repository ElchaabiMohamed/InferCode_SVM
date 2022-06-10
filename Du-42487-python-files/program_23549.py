def countdown(num):
    import time

    if num == 1:
        print(num)
        time.sleep(0.1)
        print('LIFT OFF!')
    else:
        print(num)
        time.sleep(0.1)
        countdown(num - 1)

if __name__ == '__main__':
    print(countdown(3))

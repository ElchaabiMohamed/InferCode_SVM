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

def search(str, letter):
    if str == "":
        return False
    elif str[0] == letter:
        return True
    else:
        return search(str[1:], letter)

if __name__ == '__main__':
    print(search('test', 'e'))
    print(search('test', 'a'))

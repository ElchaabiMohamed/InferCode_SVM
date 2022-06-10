def countdown(num):
    while num != 0:
        print(num)
        num -= 1
    print("LIFT OFF!")

def search(str,letter):
    i = 0
    while i < len(str):
        if str[i] == letter:
            return "True"
        i += 1
    return False

def index(str,letter):
    if letter not in str:
        return -1
    else:
        count = 0
        while str[count] != letter:
            count += 1
    return count

def fibonacci(n):
    values = [0,1]
    i = 2
    while i <= n:
        values.append(values[i - 1] + values[i - 2])
        i = i + 1
    return values[n]



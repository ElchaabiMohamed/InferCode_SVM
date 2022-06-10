def countdown(num):
    if num == 0:
        print("LIFT OFF!")
    else:
        print(num) 
        countdown(num - 1)
 
def search(str, letter):
    if str == "":
        return False
    elif str[0] == letter:
        return True
    else:
        return search(str[1:],letter)

def index(str, letter):
    if letter in str:
        return str.find(letter)
    elif letter not in str: 
        return "-1"
    else:
        return index(str[1:], letter)
        
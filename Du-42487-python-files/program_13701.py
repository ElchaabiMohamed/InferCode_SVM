def countdown(n):
  if n == 1:
    print("1")
  else:
    print(n - 1)
    countdown(n-1)

def search(string,letter):
  if string ==[]:
    return False
  elif string[0] == letter:
    return True
  else:
    return search(string[1:],letter)
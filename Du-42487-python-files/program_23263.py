def countdown(n):
  if n == 1:
    print("1")
    print("LIFT OFF!")
  else:
    print(n) 
    countdown(n-1)

def search(string,letter,pos):
  if pos == len(string):
    return False
  elif string[pos] == letter:
    return True
  else:
    return search(string,letter,pos+1)
def countdown(n):
  if n == 1:
    print("1")
    print("LIFT OFF!")
  else:
    print(n) 
    countdown(n-1)

def search(ls,val):
  if ls == []:
    return False
  elif ls[0] == val:
    return True
  else:
    return search(ls[0:],val)

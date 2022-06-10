def swap(a, i="", j=""):
  if i == ""  and j == "":
    i = 0
    j = len(a) - 1
    k = 0
    while k < (len(a)/2):
      a[i], a[j] = a[j], a[i]
      i += 1
      j -= 1
      k += 1
  else:
    a[i], a[j] = a[j], a[i]
  return a  

def reverse(a):
  return swap(a)

def swap(a, i, j):
  a = input()
  i = eval(input())
  j = eval(input())

  while a != "":
    a[i] = a[j]
    a[j] = a[i]

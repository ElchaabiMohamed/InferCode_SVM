def swap(a, i, j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp

def reverse(a):
   i = 0
   while i < len(a) / 2:
      swap(a, i, len(a)-1-i)
      i += 1

#swap(a, 0, 1)

#tmp = a[i] -> tmp = 1
#a[i] = a[j] -> [2, 2, 3, 4]
#a[j] = tmp -> [2, 1, 3, 4]

def main():
   a = [1, 2, 3, 4, 5]
   print(a)
   swap(a, 2, 3)
   print(a)
   reverse(a)
   print(a)

if __name__ == "__main__":
   main()

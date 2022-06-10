
#!usr/bin/env python

def selection_sort(a):
   i = 1
   while i < len(a):
      smallest = i
      j = i + 1
      while j < len(a):
         if a[i] < a[smallest]:
            smallest = i
         j = j + 1

      temp = a[i]
      a[i] = a[j]
      a[j] = temp
      i = i + 1

def main():
   a = [4, 3, 2, 1]
   print(selection_sort(a))

if __name__ == '__main__':
   main()

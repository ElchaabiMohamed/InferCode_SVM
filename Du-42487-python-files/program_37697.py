import sys


def count_letters(s):
   counter = 0
   if s == "":
      return 0
   else:
      for c in s:
         counter += 1
   return counter



def main():
    len = None
    print((count_letters('cat')))
    print((count_letters('catastrophe')))
    print((count_letters('')))

if __name__ == '__main__':
    main()

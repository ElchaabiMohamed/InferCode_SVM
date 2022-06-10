def count_letters(word,count = 0):
   if word == "":
      return count
   else:
      word = word[1:]
   return count_letters(word,count + 1) 




def main():
    len = None
    print((count_letters('cat')))
    print((count_letters('catastrophe')))
    print((count_letters('')))

if __name__ == '__main__':
    main()

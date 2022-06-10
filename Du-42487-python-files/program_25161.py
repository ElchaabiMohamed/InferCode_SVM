def maximum(numbers):
   if len(numbers) == 1:
      return numbers[0]

   if numbers[0] > numbers[1]:
      numbers.remove(numbers[1])
   
   else:
      numbers.remove(numbers[0])
   
   return maximum(numbers)

def main():
    max = None
    print((maximum([6,5,1,3,4])))
    print((maximum([6,5,11,3,4])))
    print((maximum([6,15,11,13,14])))
    print((maximum([6,15,11,13,4])))

if __name__ == '__main__':
    main()

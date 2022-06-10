def get_price(age):
  kids = "5" 
  oap = "7"
  normal = "10"

  if age <= 16:
    print(kids)
  
  elif age >= 60:
    print(oap)

  else:
    print(normal)


def merge_lists(l1, l2):
   l3 = []
   for token in range(1, len(l1), 2):
      print(l1[token])

   for i in range(1, len(l2), 2):
      print(l2[i])

#merge_lists([1,2,3,4], [5,6,7,8])

def weird_case(some_str):
   sen = ""
   i = True
   for letter in some_str:
      if i:
         sen += letter.upper()

      else:
         sen += letter.lower()

      if letter != " ":
         i = not i

   print(sen)

def remove_zeros(nums):
   i = 0
   while i < len(nums):
      if int(nums[i]) == 0:
         del nums[i]
      i = i + 1

   
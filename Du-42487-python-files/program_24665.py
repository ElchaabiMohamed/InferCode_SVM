def get_price(age):
  kids = "5 euro" 
  oap = "7 euro"
  normal = "10 euro"

  if age <= 16:
    print(kids, "euro")
  
  elif age >= 60:
    print(oap, "euro")

  else:
    print(normal, "euro")


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

   
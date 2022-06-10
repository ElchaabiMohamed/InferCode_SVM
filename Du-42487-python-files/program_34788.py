def get_price(age):
  kids = "5" 
  oap = "7"
  normal = "10"

  if age <= 16:
    return kids
  
  elif age >= 60:
    return oap

  else:
    return normal


def merge_lists(l1, l2):
   l3 = []
   for token in range(0, len(l1), 2):
      l3.append(l1[token])


   for i in range(0, len(l2), 2):
      l3.append(l2[i])

   return l3

#merge_lists([4,5,6], [7,8])

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

   return sen

def remove_zeros(nums):
   gway = []
   i = 0
   while i < len(nums):
      if int(nums[i]) != 0:
         gway.append(nums[i])  
      i = i + 1
   nums = gway
   return nums

#remove_zeros([0,0,9])
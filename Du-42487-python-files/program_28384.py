def countdown(num):
   if num == 0:
      print("LIFT OFF!")
   else:
      print(num)
      countdown(num - 1)

def search(str, letter):
   if str == "":
      return "False"
   elif str[0] == letter:
      return "True"
   else:
      return search(str[1:], letter)

def reverse(list):
 reversed = []

 i = len(list) - 1
 while i >= 0:
  reversed.append(list[i])
  i = i - 1
 
 return reversed

#!/usr/bin/env python

#Function 1:
def get_price(age): 
   if age < "17":
      return "5"
   elif age >= "60": 
      return "7"
   else:
      return "10"

if __name__ == '__main__':
   print('calling get_price(\'age\')')
   print(get_price('age')) 

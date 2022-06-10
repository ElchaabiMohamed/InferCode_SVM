def get_price(age):
  if int(age) <= 16:
    print("€5")
  if int(age) >= 60:
    print("€7")
  else:
    print("€10")




if __name__ == '__main__':
   print('calling weird_case(\'change the case\')')
   print(weird_case('change the case'))
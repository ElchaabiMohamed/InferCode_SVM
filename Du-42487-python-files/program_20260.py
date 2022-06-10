def get_price(age):
  if int(age) <= 16:
    return "€5"
  if int(age) >= 60:
    return "€7"
  else:
    return "€10"




if __name__ == '__main__':
   print('calling weird_case(\'change the case\')')
   print(weird_case('change the case'))
def merge_lists(l1,l2):
  '''take two lists l1 and l2 and return a third list which contains 
  every second element of l1 and l2'''
  l3 = []
  i = 0
  while i < len(l1):
      l3.append(l1[i])
      i += 2
  i = 0
  while i < len(l2):
      l3.append(l2[i])
      i += 2
  return l3

def weird_case(some_str):
    '''takes a string some_str and contains a new string which is the same as some_str but the case alternates between upper and lower'''
    new_str = ""
    i = 0
    lc = 0 # separate count for the letters
    while i < len(some_str):
        if some_str[i].isalpha():
            if lc % 2 == 0:
                new_str += some_str[i].upper()
            else:
                new_str += some_str[i].lower()
            lc += 1
        else:
          new_str += some_str[i]
        i = i + 1
    return new_str

def remove_zeros(list):
    '''remove zeros from list'''
    while 0 in list:
        list.remove(0)

def get_price(age):
    '''checks age and returns price associated with the age'''
    if age <= 16:
        return 5
    elif age <=60:
        return 10
    else:
        return 7

def search(str,sub):
  '''returns the position of sub in str, -1 if it is not there'''
  i = 0
  while i < len(str):
    if sub == str[i]:
      return i
    i = i + 1
  return -1

def countdown(num):
  '''prints all the numbers from num to 0'''
  while num >= 0:
    print(num)
    num = num - 1

def fibonacci(n):
  '''returns the value of the fibonnaci series at position n'''
  if n == 0:
    return 1
  elif n == 1:
    return 1
  else:
    fibN_2 = 1
    fibN_1 = 1
    i = 2
    while i <=n:
      fibN = fibN_2 + fibN_1
      fibN_2 = fibN_1
      fibN_1 = fibN
      i = i + 1
    return fibN

if __name__ == '__main__':
  print('testing get_price')
  print(get_price(7))

  print('testing merge_lists')
  print(merge_lists(['a','x'],['b','y']))

  print('testing weird_case')
  print(weird_case('test'))

  print('testing remove_zeros')
  l = [0,0,9]
  print(l)
  remove_zeros(l)
  print(l)

  print('testing countdown')
  countdown(10)

  print('testing search')
  print(search('test','t'))
  print(search('test','a'))

  print('testing fibonacci')
  print(fibonacci(5))

   
    



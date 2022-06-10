def swap(a, i, j):

  tmp = a[i]
  a[i] = a[j]
  a[j] = tmp

def find_position_of_smallest(a, i):
  
  smallest = a[i]
  
  while i < len(a):
    if smallest < a[i +1]:
      smallest = smallest
    elif smallest > a[i + 1]:
      smallest = a[i + 1]
  i = i + 1

print(smallest)

    

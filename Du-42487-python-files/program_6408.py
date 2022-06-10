
def bsearch(a,q):
  low =0
  high= len(a)
  
  while low < high:
    mid= (low + high)/ 2
    assert low <= mid < high
    
    if a[mid] < q:
      low = mid + 1
      
    else:
      high=mid
      
  return low
    
def bsearch(a,q): #make function
   low = 0
   high = len(a)

   while low < high:
      mid = (low + high) / 2
      # take the middle number. mid and high are never equal
      # mid is always valid index in a because 0<=mid<high
      # either low is going to progress, or high is going to progress

      if a[mid] < q: # is value less than q? NOT equal to
         low = mid + 1 # the +1 here is really important!!
      else:
         high = mid

   return low
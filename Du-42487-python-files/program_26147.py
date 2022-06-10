def bsearch(a,q):
   low=0
   high=len(a)
   i=0
   while low!=high:
      mid=(high+low)/2
      if a[mid]<q:
         high=mid
      else:
         low=mid
   return low

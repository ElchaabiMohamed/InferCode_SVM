def bsearch(a,q):
   low=0
   high=len(a)
   i=0
   if q in a:
      while a[i]!=q:
         i+=1
      print(i)
   else:
      while low!=high:
         mid=(high+low)/2
         if a[mid]<low:
            high=mid
         else:
            low=mid
         return low

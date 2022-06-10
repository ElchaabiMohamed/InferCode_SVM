def minimum(a):
   if len(a) == 1:
      return a[0]
   else:
      nl = minimum(a[1:]) #4 3
   if a[0] < nl:
      return a[0]
   else:
      return nl


#[6,5,1,3,4]

#[4]         4
#[3,4]       3
#[1,3,4]     1
#[5,1,3,4]



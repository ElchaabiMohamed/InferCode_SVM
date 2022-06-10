#attempt #1(too complicated)
#def swap(a,i,j):
#   track=0
#   templist=[]
#   while track!=len(a):
#      if track == i:
#         templist.append(a[j])
#      elif track == j:
#         templist.append(a[i])
#      else:
#         templist.append(a[track])
#      track=track+1
#   a=templist
#   return a
#<><><><><><><>

#Swap()
def swap(a,i,j):
    temp=a[i]
    a[i]=a[j]
    a[j]=temp

#find_position_of_smallest()
def find_position_of_smallest(a,i):
   track=0
   tempnum=a[i+track]
   while track!=(len(a)-i):
      if a[i+track] == tempnum:
         tempnum=a[i+track]
      track=track+1
   return tempnum
#sort()
def sort(a):
   i=0
   j=0
   while i !=len(a):
      j=find_position_of_smallest(a,i)
      swap(a,i,j)
      i=i+1
#test


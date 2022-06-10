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
   tempnum=i
   while i!=len(a):
      if a[i] < a[tempnum]:
         tempnum=i
      i=i+1
   return tempnum
#test
a=[0,1,3,2]
print(find_position_of_smallest(a,2))

#sort()
def sort(a):
   i=0
   j=0
   while i !=len(a):
      j=find_position_of_smallest(a,i)
      swap(a,i,j)
      i=i+1



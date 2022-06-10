def smallest(a,i):
   p = i
   j = i + 1
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j += 1
   return p

def swap(a,i,p):
   tmp = a[p]
   a[p] = a[i]
   a[i] = tmp

def selectionsort(a):
   i = 0
   while i < len(a):
      p = smallest(a,i)
      swap(a,i,p)
      i += 1
   return a

#def selectionsort(a):
#
#   if(len(a) != 2):
#      a = [[], a]#
#
#   mini = min(a[1])
#   a[1].remove(mini)
#   a[0].append(mini)
#   if len(a[1]) == 0:
#      return a[0]
#      
#   else:
#      return selectionsort(a)



import random
def main():
    A = random.sample(list(range(-99, 100)), 10)

    print(('Unsorted: {}'.format(A)))
    
    print(('Sorted: {}'.format(selectionsort(A))))

if __name__ == '__main__':
    main()
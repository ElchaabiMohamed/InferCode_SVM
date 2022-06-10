def selection_sort(a):
   i = 0
   while i < len(a):
      p = find_smallest_position(a,i)
      swap(a,i,p)
      i = i + 1

def main():
    print(selection_sort([3,5,1,7,4]))

if __name__=="__main__":
    main()

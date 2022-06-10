def selection_sort(a):
   i = 0
   while i < len(a):
      p = find_smallest_position(a,i)
      swap(a,i,p)
      i = i + 1
      return a 

def main():
   print(selection_sort(a))

if __name__ == "__main__":
   main()
def swap(a,i,j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp
    return a 
def reverse(a):
    i = 0
    while i < len(a) / 2:
        j = a[len(a) - i - 1]
        swap(a,i,j)
        i = i + 1

        

def main():
   print(double(5))
   print(double("Hello"))

if __name__ == "__main__":
   main()
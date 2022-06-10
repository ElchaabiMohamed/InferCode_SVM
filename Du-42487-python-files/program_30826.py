a = [9,0,8,7,4,20,6,5,4,3,13,2,1]

def swap(a,i,p):
    tmp = a[p]
    a[p] = a[i]
    a[i] = tmp

def reverse(a,i):
    p = i
    j = i + 1
    while j < len(a):
        if int(a[j]) > int(a[p]):
            p = j
        j = j + 1
    return p
    
i = 0
while i < len(a):
    p = reverse(a,i)
    swap(a,i,p)
    i = i + 1
    
def main():
    print(a)
    
if __name__ == "__main__":
    main()
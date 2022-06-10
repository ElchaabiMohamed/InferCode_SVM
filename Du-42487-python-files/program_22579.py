def append2list(w, alist=[]):
    alist.append(w)
    return alist

def main():    
    word = 'banana'
    nlist = append2list(word, 'apple')
    print(nlist)
    word = 'orange'
    nlist = append2list(word, 'pineapple')
    print(nlist)
    word = 'mango'
    nlist = append2list(word, 'coconut')
    print(nlist)

if __name__ == '__main__':
    main()


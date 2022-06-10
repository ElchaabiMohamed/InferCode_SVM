def swap_unique_keys_values(d):
    items=set(d.items())
    for w in items:
        if items.count(w)>1:
	         d.pop(d[w])
    print(items)
    d={v:k for (k,v) in list(d.items())}
    return(d)


def main():
 	swap_unique_keys_values(items)


if __name__=="__main__":
 	main()

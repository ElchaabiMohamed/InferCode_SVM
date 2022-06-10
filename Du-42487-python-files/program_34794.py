
def swap_unique_keys_values(d):
    print((list(d.items())))
    for w in list(d.items()):
    	if list(d.items()).count(w)>1:
    		d.popitem(d[w])	
    d={v:k for (k,v) in list(d.items())}
    return(d)



def main():
	swap_unique_keys_values()

if __name__=="__main__":
	main()

def swap_unique_keys_values(d):
    for w in list(d.keys()):
    	if list(d.keys()).count(w)>1:
    		d.popitem(d[w])
    d={v:k for (k,v) in list(d.items())}
    return(d)



def main():
	swap_unique_keys_values()

if __name__=="__main__":
	main()

def swap_unique_keys_values(d):
    print((list(d.keys())))
    for w in list(d.items()):
    	if list(d.items()).count(w)>1:
    		d.popitem(d[w])	
   #d={v:k for (k,v) in d.items()}
    
    return(d)



def main():
	swap_unique_keys_values()

if __name__=="__main__":
	main()
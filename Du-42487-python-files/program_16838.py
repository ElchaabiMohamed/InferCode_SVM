def swap_keys(d):
	d={v:k for (k,v) in list(d.items())}
	return(d)

def main():
	swap_keys()

if __name__=="__main__":
	main()		
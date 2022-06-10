import sys
def swap_keys_values(d):
	new={}
	for (z,q) in (list(d.items())):
		new[q]=z
	return(list(new.items()))
def main():
	d={1:"op",}
	print((swap_keys_values(d)))
if __name__=="__main__":
	main()

	

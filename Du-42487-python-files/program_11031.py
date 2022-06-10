import sys

def overlap(x1=None,y1=None,r1=None,x2=None,y2=None,r2=None):	
	if x1 is None:
		x1=0
	elif y1 is None:
		y1=0
	elif r1 is None:
		r1=1
	
	if (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)<(r1+r2)*(r1+r2):
		return(True)
	else:
		return(False)
       

def main():
    print((overlap(int(sys.argv[1]))))

if __name__=="__main__":
	main()
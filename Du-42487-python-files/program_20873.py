import sys

	
def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
	distance = (abs((x2-x1)**2) + abs((y2-y1)**2))**0.5
	#print(distance)
	if r1 + r2 > distance:
		return True
	else:
		return False

def main():
	pass
	
if __name__ == "__main__":
	main()
#print(overlap(10,0,1,8,0,1))
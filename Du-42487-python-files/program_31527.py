

def reverse(a):
	b = []
	while len(a) != 0:
		b.append(a.pop())
	return b


if __name__ == "__main__":
  print(reverse([1,2,3]))
  print(reverse(["a", "b"]))
	


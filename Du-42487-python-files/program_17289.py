def minimum(a, minimum = None):
  if not a:
    return minimum
  test = a.pop()
  if test < minimum or minimum == None:
    return minimum(a, test)
  else:
    return minimum(a, minimum)

def main():
  minimum()

if __name__ == "__main__":
  main()

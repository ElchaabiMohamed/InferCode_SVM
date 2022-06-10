def minimum(a, minimum = 0):
  if not a:
    return minimum
  test = a.pop()
  if test < minimum or minimum == 0:
    return minimum(a, test)
  return minimum(a, minimum)

def main():
  minimum()

if __name__ == "__main__":
  main()

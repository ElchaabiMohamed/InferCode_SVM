def minimum(a, minimum = 0):
  if not a:
    return minimum
  test = str(a.pop())
  if int(test) < int(minimum) or int(minimum) == 0:
    return minimum(a, test)
  return minimum(a, minimum)

def main():
  minimum()

if __name__ == "__main__":
  main()

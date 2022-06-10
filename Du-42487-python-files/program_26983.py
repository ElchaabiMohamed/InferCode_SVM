def maximum(a, high = 0):
  if not a:
    return high
  test = a.pop()
  if test > high or high == 0:
    return maximum(a, test)
  return maximum(a, high)

def main():
  maximum()

if __name__ == "__main__":
  main()

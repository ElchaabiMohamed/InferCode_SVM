def minimum(a, mini = 0):
  if not a:
    return mini
  test = a.pop()
  if test < mini or mini == 0:
    return minimum(a, test)
  return minimum(a, mini)

def main():
  minimum()

if __name__ == "__main__":
  main()

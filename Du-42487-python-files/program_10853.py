def reverse_list(a):
  if len(a) == 0:
    return []
  else:
    return [a[-1]] + reverse_list(a[:-1])

def main():
  reverse_list()

if __name__ == "__main__":
  main()

def count_letters(s):
  if s == "":
    return 0
  return 1 + count_letters(s[:-1])

def main():
  count_letters()

if __name__ == "__main__":
  main()

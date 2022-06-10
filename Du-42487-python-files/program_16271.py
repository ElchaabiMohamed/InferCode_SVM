import sys

def swap_keys_values(d):
  return {v : k for (k, v) in list(d.items())}

def main():
  swap_keys_values()

if __name__ == "__main__":
  main()

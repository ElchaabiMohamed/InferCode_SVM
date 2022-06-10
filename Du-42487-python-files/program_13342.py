import sys

def swap_unique_keys_values(d):
  seen = []
  return {v : k for (k, v) in list(d.items())}

def main():
  swap_unique_keys_values()

if __name__ == "__main__":
  main()

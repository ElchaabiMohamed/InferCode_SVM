import sys

def swap_keys_values(d):
  return{v : k for (k, v) in list(d.items())}

def main():
  d = {
          "a" : 4,
          "b" : 7,
          "c" : 10
  }
  print((swap_key_values(d)))

if __name__=="__main__":
    main()

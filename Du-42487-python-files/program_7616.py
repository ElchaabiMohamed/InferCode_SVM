import sys

def main():
    with open(sys.argv[1], 'r') as f:
        d=f.read()
    print(d)
    inv = {v: k for k, v in list(d.items())}
    print(inv)

if __name__ == '__main__':
    main()

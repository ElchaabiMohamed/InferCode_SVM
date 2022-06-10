def swap_unique_keys_values(d):
    return(set({v : k for (k, v) in d}))

def main():
    print((swap_unique_keys_values(d)))
    
if __name__ == "__main__":
    main()

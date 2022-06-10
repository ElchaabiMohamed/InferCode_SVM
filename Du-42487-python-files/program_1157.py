def swap_key_values(d):
    d={v:k for (k,v) in list(d.items())}
    return(d)


def main():
	swap_key_values()


if __name__=="__main__":
	main()
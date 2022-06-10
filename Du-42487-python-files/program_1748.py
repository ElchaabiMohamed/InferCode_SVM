def sumup(n):
    if n == 0: # base case : no more calls to sum_up_to()
        return 0
    return n + sumup(n-1)

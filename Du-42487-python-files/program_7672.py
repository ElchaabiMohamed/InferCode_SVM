def fibonacci(a):
    prev = 1
    curr = 1
    tmp = 0
    i = 0
    for i in range(0, a):
        tmp = curr
        curr = prev + curr
        prev = tmp
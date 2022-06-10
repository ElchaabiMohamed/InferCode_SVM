def fibonacci(value):
    if value == 1 or value == 0:
        return 1

    return fibonacci(value - 1) + fibonacci(value - 2)
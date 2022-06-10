def fibonacci(n, first_number=0, second_number=1, counter=0):
    if n == 0:
        print("HEYA")
        return 0
    elif n == 1:
        return 1
    elif n == counter:
        return second_number
    else:
        holder = second_number
        second_number += first_number
        first_number = holder
        return fibonacci(n, first_number, second_number, counter + 1)


count = 0
while count != 100:
    if count % 3 == 0:
       print("fizz")
    elif count % 5 == 0:
       print("buzz")
    elif count % 3 and 5 == 0:
       print("fizzbuzz")
    else: 
       print(count)
    count = count + 1

import sys
n = sys.stdin.readlines()
i = 0

if n[i] % 3 == 0:
  print('Fizz')
elif n[i] % 5 == 0:
  print('Buzz')
elif n[i] % 3 == 0 and n % 5 == 0:
  print('FizzBuzz')
else:
  print(n[i])
i = i + 1


def countdown(n):
  if n == 0:
    return "LIFT OFF!"
  print(n - 1)
  countdown(n-1)

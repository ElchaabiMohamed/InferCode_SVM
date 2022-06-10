
def countdown(n):
  if n == 1:
    return "LIFT OFF!"
  print(n - 1)
  countdown(n-1)

import sys

def swap_keys_values(n):
  dic ={}
  for key in n:
    dic[n[key]] = key
  return dic
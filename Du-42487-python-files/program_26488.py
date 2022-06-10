import sys

def swap_dic(n):
  dic ={}
  for key in n:
    dic[n[key]] = key
  return dic
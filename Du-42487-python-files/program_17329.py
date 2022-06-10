def reverse_list(listt):
   if not listt:
      return listt
   else:
      return([listt[-1]] + reverse_list(listt[:-1]))

if __name__ == "__main__":
   print((reverse_list([1, 2,3])))

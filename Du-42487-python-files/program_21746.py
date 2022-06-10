def swap_unique_keys_values(n):
  dic = {}
  values = []
  no_uni = []
  for key in n:
    if n[key] in values:
      no_uni.append(n[key])
    else:
      values.append(n[key])
  for key in n:
    if not n[key] in no_uni:
      dic[n[key]] = key
  return dic
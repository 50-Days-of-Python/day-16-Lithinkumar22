def sum_list(l):
  s = 0
  a = []
  for i in l:
    a.extend(i)
  for j in a:
    s = s + j
  
  return s


def find_max_min(y):
  minm = y[0]
  maxm = y[0]
  for x in y[1:]:
    if x < minm:
      minm = x
    elif x > maxm:
      maxm = x
    else:
      if minm == maxm:
        return [len(y)]
  return [minm, maxm]


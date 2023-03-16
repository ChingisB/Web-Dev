def lone_sum(a, b, c):
  if a == b:
    if a == c:
      return 0
    return c
  if b == c:
    return a
  if a == c:
    return b
  return a + b + c

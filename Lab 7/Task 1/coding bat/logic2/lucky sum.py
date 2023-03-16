def lucky_sum(a, b, c):
  ans = 0
  if a == 13:
    return 0
  ans += a
  if b == 13:
    return ans
  ans += b
  if c == 13:
    return ans
  return ans + c
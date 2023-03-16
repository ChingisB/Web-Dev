def missing_char(str, n):
  ans = ""
  for i in range(len(str)):
    if i == n:
      continue
    ans += str[i]
  return ans

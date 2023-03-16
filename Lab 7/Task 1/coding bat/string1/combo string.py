def combo_string(a, b):
  a, b = min(a, b, key=len), max(a, b, key=len)
  return a + b + a

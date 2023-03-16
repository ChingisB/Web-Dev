def count_code(str):
  cnt = 0
  for item in set(str):
    cnt += str.count("co" + item + "e")
  return cnt
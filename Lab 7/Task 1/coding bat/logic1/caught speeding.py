def caught_speeding(speed, is_birthday):
  if speed <= 60 or (is_birthday and speed <= 65):
    return 0
  if 61 <= speed <= 80 or (is_birthday and 66 <= speed <= 85):
    return 1
  if speed >= 81 or (is_birthday and speed >= 86):
    return 2
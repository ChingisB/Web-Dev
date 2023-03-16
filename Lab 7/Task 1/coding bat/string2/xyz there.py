def xyz_there(str):
  if 'xyz' not in str:
    return False
  return str.count(".xyz") != str.count("xyz")

def valid_anagram(array_one, array_two):
  if len(array_one) != len(array_two):
    return False

  count = 1

  array_one_dict = {}
  array_two_dict = {}
  for letter in array_one:
    if letter not in array_one_dict:
      array_one_dict[letter] = count
    else:
      array_one_dict[letter] = count + 1

  for letter in array_two:
    if letter not in array_two_dict:
      array_two_dict[letter] = count
    else:
      array_two_dict[letter] = count + 1

  for key in array_one_dict.keys():
    if key not in array_two_dict.keys():
      return False
    if array_one_dict[key] != array_two_dict[key]:
      return False

  return True


print(valid_anagram('silent', 'listen'))
def find_index(to_search, target):
  for i, value in enumerate(to_search):
    if value == target:
      break
  else:
    return -1
  return i


my_list = ['Dams', 'Aditya', 'Adesh','Niket','Devendra','Tanmay']
index_location = find_index(my_list, 'Dams')

print('Location of target is index: {}'.format(index_location))

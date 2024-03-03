import os

def write_list_to_file(filename, data_list, directory=None):
  if directory and not os.path.exists(directory):
    os.makedirs(directory)

  global filepath
  filepath = os.path.join(directory or "", filename)
  with open(filepath, 'w') as file:
    for item in data_list:
      file.write(str(item) + '\n')
data_list = ["item1", "item2", 3, 4.5]
filename = "task5.txt"
directory = "./dir-and-files/textfiles/"

write_list_to_file(filename, data_list, directory)

print(f"Data written to {filepath}")

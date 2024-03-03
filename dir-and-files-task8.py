import os

def delete_file_with_checks(path):
  if not os.path.exists(path):
    print(f"Error: File '{path}' does not exist.")
    return False

  if not os.access(path, os.W_OK):
    print(f"Error: Permission denied. You don't have write access to '{path}'.")
    return False

  try:
    os.remove(path)
    print(f"File '{path}' deleted successfully.")
    return True
  except OSError as e:
    print(f"Error deleting file '{path}': {e}")
    return False

file_path = "dir-and-files/textfiles/task7.txt"

if delete_file_with_checks(file_path):
  print("File deletion successful.")
else:
  print("File deletion failed.")

import os

def list_directories(path, only_dirs=True):
  for item in os.listdir(path):
    item_path = os.path.join(path, item)
    if os.path.isdir(item_path) and (not only_dirs or not item.startswith('.')):
      print(item_path)

path = "\."
print("Listing directories only:")
list_directories(path)

print("\nListing all directories and files:")
list_directories(path, only_dirs=False)

import os

def copy_file(source_file, destination_file, destination_directory=None):
 destination_path = os.path.join(destination_directory or "", destination_file)

 try:
   if destination_directory and not os.path.exists(destination_directory):
     os.makedirs(destination_directory)

   with open(source_file, 'r') as source, open(destination_path, 'w') as destination:
     destination.write(source.read())

   print(f"File copied successfully from {source_file} to {destination_path}")

 except FileNotFoundError as e:
   print(f"Error: Source file not found: {e}")
 except OSError as e:
   print(f"Error during file copying: {e}")

source_file = "dir-and-files/textfiles/task5.txt"
destination_file = "task7.txt"
destination_directory = "dir-and-files/textfiles"

copy_file(source_file, destination_file, destination_directory)

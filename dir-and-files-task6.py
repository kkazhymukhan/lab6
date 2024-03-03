import string
import os

def generate_text_files(directory, start_letter="A", end_letter="Z"):
  if not os.path.exists(directory):
    os.makedirs(directory)

  for letter in string.ascii_uppercase[string.ascii_uppercase.index(start_letter): string.ascii_uppercase.index(end_letter) + 1]:
    filename = f"{letter}.txt"
    filepath = os.path.join(directory, filename)

    with open(filepath, "w") as _:
      pass

directory = "./dir-and-files/textfiles/task6"

generate_text_files(directory)

print(f"Text files generated from A to Z in {directory}")

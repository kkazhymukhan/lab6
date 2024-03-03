def count_lines(filename):
  try:
    with open(filename, 'r') as file:
      lines = file.readlines()
      return sum(1 for line in lines)
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    return None

# Example usage
filename = "C:\Setup.log"
num_lines = count_lines(filename)

if num_lines is not None:
  print(f"Number of lines in '{filename}': {num_lines}")

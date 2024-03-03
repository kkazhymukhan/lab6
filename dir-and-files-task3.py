import os

def check_path(path):
  result = {"exists": False, "filename": None, "directory": None}
  if os.path.exists(path):
    result["exists"] = True
    result["filename"] = os.path.basename(path)
    result["directory"] = os.path.dirname(path)
  return result

path = "C:\ASTRONEER\Astro.exe"

path_info = check_path(path)

print(f"Path: {path}")
print(f"Exists: {path_info['exists']}")
if path_info['exists']:
  print(f"Filename: {path_info['filename']}")
  print(f"Directory: {path_info['directory']}")

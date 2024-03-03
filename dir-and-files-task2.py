import os

def check_path_access(path):
  access_info = {
      "exists": os.path.exists(path),
      "readable": os.access(path, os.R_OK),
      "writable": os.access(path, os.W_OK),
      "executable": os.access(path, os.X_OK) if os.path.isfile(path) else False,
  }
  return access_info


path = "C:\ASTRONEER\Astro.exe"

access_info = check_path_access(path)

print(f"Path: {path}")
for permission, status in access_info.items():
  print(f"{permission}: {status}")

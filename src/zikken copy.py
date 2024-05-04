from pathlib import Path
import sys
import os
# sys.path.append(str(Path(__file__).parent / "scenes"))
# sys.path.append(str(Path(__file__).parent / "user_interface"))

check_path = [
    "scenes",
    "user_interface"
]

for dir_name in check_path:
    path = str(Path(__file__).parent / dir_name)
    if not os.path.exists(path):
        print(f"Do not exists: {path}")
        exit()
    sys.path.append(path)

print("ALL OK!!")

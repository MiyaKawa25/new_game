import os
import sys


def append_tile_path():
    sys.path.append(
        os.path.join(SRC_PATH, "resources", "worlds", "tile"))


CURRENT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
path_arr = CURRENT_DIR_PATH.split("/")

# new_gameの絶対パスを取得
PROJECT_PATH = "/"
for path in path_arr:
    PROJECT_PATH = os.path.join(PROJECT_PATH, path)
    if path == "new_game":
        break

# src/の絶対パスを取得
SRC_PATH = os.path.join(PROJECT_PATH, "src")
sys.path.append(SRC_PATH)

# tile/の追加
append_tile_path()


if __name__ == "__main__":
    print(f"CURRENT_DIR_PATH: {os.path.split(CURRENT_DIR_PATH)}")
    print(f"CURRENT_DIR_PATH: {CURRENT_DIR_PATH}")
    print(f"PROJECT_PATH: {PROJECT_PATH}")
    print(f"    SRC_PATH: {SRC_PATH}")

"""path_optionのルール

1. 処理の追加はプロジェクト直下のファイルで行うこと
    ※ 基本的な構造を統一するため

2. 新しい場所にこのファイルを作りたい場合はMakefileでコピーする
    ※実行するときに上書き確認が出るので関係ないばじょは'n'を押すこと

3. 以下のコマンドで他の場所のpath_option.pyに上書きする
    $ make path_option_normalization

4. 実際に読み込まれるpath_optionで使わないパスの追加処理はコメントする
    # 関数呼び出し部分をコメントにする
"""


import os
import sys


def append_tile_path():
    sys.path.append(
        os.path.join(RESOURCES_PATH, "worlds", "tile"))


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


# resources/ のパスを取得
RESOURCES_PATH = os.path.join(PROJECT_PATH, "resources")



# tile/の追加
append_tile_path()

if __name__ == "__main__":
    print(f"CURRENT_DIR_PATH: {os.path.split(CURRENT_DIR_PATH)}")
    print(f"CURRENT_DIR_PATH: {CURRENT_DIR_PATH}")
    print(f"PROJECT_PATH: {PROJECT_PATH}")
    print(f"    SRC_PATH: {SRC_PATH}")

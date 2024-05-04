help:
	@echo "ゲームを開始する"
	@echo " $$ make run"

# ゲーム実行
run:
	poetry run python3 src
game:
	poetry run python3 src/game.py
title:
	poetry run python3 src/scenes/title.py
map:
	poetry run python3 src/scenes/map_scene.py

# フォーマット
format:
	poetry run python -m autopep8 -i -r src/

# その他
zikken:
	poetry run python3 src/zikken.py

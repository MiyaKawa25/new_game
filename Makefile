help:
	@echo "ゲームを開始する"
	@echo " $$ make run"

# ゲーム実行
run:
	poetry run python3 src
game:
	poetry run python3 src/game.py
title:
	poetry run python3 src/game_title.py
story1:
	poetry run python3 src/story_01.py

# フォーマット
format:
	poetry run python -m autopep8 -i -r src/

# その他
zikken:
	poetry run python3 src/zikken.py

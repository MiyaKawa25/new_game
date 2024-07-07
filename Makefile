RESOURCE_MAP_PATH := resources/worlds/maps


help:
	@echo "ゲームを開始する"
	@echo " $$ make run"
	@echo "フォーマットする"
	@echo " $$ make format"
	@echo "パス設定ファイルの正規化"
	@echo " $$ make path_option_normalization"
	@echo "タイルマップの作成・編集"
	@echo " $$ make create_map"

# ゲーム実行
run:
	poetry run python3 src

# フォーマット
format:
	poetry run python -m autopep8 -i -r src/

path_option_normalization:
	cp -i path_option.py src/scenes/path_option.py
	cp -i path_option.py src/user_interface/path_option.py

# 作業用(ゲーム実行)
title:
	poetry run python3 src/scenes/title.py

map:
	poetry run python3 src/scenes/map_scene.py

test_scene:
	poetry run python3 src/scenes/test_scene.py

draw_human:
	poetry run python3 src/interface/draw_human.py

# テスト実行
test:
	poetry run pytest tests

# その他
zikken:
	poetry run python3 src/zikken.py

# 作業用(素材作成)
create_map:
	poetry run pyxel edit $(RESOURCE_MAP_PATH)/sample

tile_map:
	poetry run python3 src/user_interface/tile_map.py

resize:
	poetry run python3 utilities/resize.py

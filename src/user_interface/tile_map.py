import pyxel
import os

CURRENT_DIR_PATH = os.path.dirname(
    os.path.abspath(__file__))  # user_interface/
PROJECT_DIR_PATH = os.path.dirname(
    os.path.dirname(CURRENT_DIR_PATH))  # new_game


class TileMap():
    """タイルマップを管理するクラス."""
    RESORCE_MAP_PATH = os.path.join(
        PROJECT_DIR_PATH, "resources", "worlds", "maps")

    @staticmethod
    def set_map(map_name="sample.pyxres"):
        pyxel.load(os.path.join(TileMap.RESORCE_MAP_PATH, map_name))


if __name__ == "__main__":
    pyxel.init(240, 180)  # (W, H)
    map_scene = TileMap()
    map_scene.set_map()

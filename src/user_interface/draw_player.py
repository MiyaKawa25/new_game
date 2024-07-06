if __name__ == "__main__":  # noqa
    from path_option import *

import os

from game_option import Option as Op
from user_interface.draw_move_object import DrawMoveObject



JSON_PATH = os.path.join(RESOURCES_PATH, "charactors", "players.json")


class DrawPlayer(DrawMoveObject):
    """操作するキャラクターの描画する座標を管理するクラス."""

    # キャラが描かれているタイルマップ上座標
    __TILE_COORDI_UP = [16, Op.window_h+16]
    __TILE_COORDI_RIGHT = [48, Op.window_h+16]
    __TILE_COORDI_DOWN = [0, Op.window_h+16]
    __TILE_COORDI_LEFT = [32, Op.window_h+16]

    # キャラのサイズ
    __CHARA_SIZE_X = 16
    __CHARA_SIZE_Y = 16

    def __init__(self,
                 first_location_x, first_location_y,
                 first_direction, move_pixel=2):
        # コンストラクタ
        super().__init__(
            tile_coordi_up=DrawPlayer.__TILE_COORDI_UP,
            tile_coordi_right=DrawPlayer.__TILE_COORDI_RIGHT,
            tile_coordi_down=DrawPlayer.__TILE_COORDI_DOWN,
            tile_coordi_left=DrawPlayer.__TILE_COORDI_LEFT,
            first_direction=first_direction,
            tile_size_x=DrawPlayer.__CHARA_SIZE_X,
            tile_size_y=DrawPlayer.__CHARA_SIZE_Y,
            first_location_x=first_location_x,
            first_location_y=first_location_y,
            move_pixel=move_pixel,
            max_hp = 100
        )

    @property
    def get_chara_size_x(cls):
        """キャラクターのXサイズを返すGetter."""
        return cls.__CHARA_SIZE_X
    
    @property
    def get_chara_size_y(cls):
        """キャラクターのXサイズを返すGetter."""
        return cls.__CHARA_SIZE_Y
    

if __name__ == "__main__":
    print(f"CURRENT_DIR_PATH: {os.path.split(CURRENT_DIR_PATH)}")
    print(f"CURRENT_DIR_PATH: {CURRENT_DIR_PATH}")
    print(f"PROJECT_PATH: {PROJECT_PATH}")
    print(f"    SRC_PATH: {SRC_PATH}")
resources/charactors
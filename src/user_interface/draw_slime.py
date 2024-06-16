if __name__ == "__main__":  # noqa
    from path_option import *

from game_option import Option as Op
from user_interface.draw_move_object import DrawMoveObject


class DrawSlime(DrawMoveObject):
    """操作するキャラクターの描画する座標を管理するクラス."""

    __TILE_COORDI_UP = [16, Op.window_h+16]
    __TILE_COORDI_RIGHT = [48, Op.window_h+16]
    __TILE_COORDI_DOWN = [0, Op.window_h+16]
    __TILE_COORDI_LEFT = [32, Op.window_h+16]

    def __init__(self,
                 first_location_x, first_location_y,
                 first_direction, move_pixel=2):
        # コンストラクタ
        super().__init__(
            tile_coordi_up=DrawSlime.__TILE_COORDI_UP,
            tile_coordi_right=DrawSlime.__TILE_COORDI_RIGHT,
            tile_coordi_down=DrawSlime.__TILE_COORDI_DOWN,
            tile_coordi_left=DrawSlime.__TILE_COORDI_LEFT,
            first_direction=first_direction,
            tile_size_x=16,
            tile_size_y=16,
            first_location_x=first_location_x,
            first_location_y=first_location_y,
            move_pixel=move_pixel
        )

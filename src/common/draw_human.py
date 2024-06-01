if __name__ == "__main__":  # noqa
    from path_option import *

from game_option import Option as Op
from common.draw_move_object import DrawMoveObject

class DrawHuman(DrawMoveObject):
    """操作するキャラクターの描画する座標を管理するクラス."""
    def __init__(self, move_pixel=2):
        # コンストラクタ
        first_coordi = [16, Op.window_h] # 最初に描画するタイル座標
        super().__init__(
            [0, Op.window_h],
            [48, Op.window_h],
            first_coordi,
            [32, Op.window_h],
            first_coordi[0],
            first_coordi[1],
            move_pixel
        )


if __name__ == "__main__":
    dh = DrawHuman()
    print(dh.get_tile_x())
    print(dh.get_tile_y())

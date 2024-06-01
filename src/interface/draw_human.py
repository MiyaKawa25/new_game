if __name__ == "__main__":  # noqa
    from path_option import *

from game_option import Option as Op


class DrawHuman:
    """操作するキャラクターの描画する座標を管理するクラス."""

    # 表示するタイル座標
    __tile_coordi_up = [0, Op.window_h]
    __tile_coordi_right = [48, Op.window_h]
    __tile_coordi_down = [16, Op.window_h]
    __tile_coordi_left = [32, Op.window_h]

    def __init__(self, move_pixel=2):
        # 表示するタイル座標
        self.__tile_x = self.__tile_coordi_down[0]
        self.__tile_y = self.__tile_coordi_down[1]
        self.__current_location_x = 0
        self.__current_location_y = 0
        self.__move_pixel = move_pixel

    def look_up(self):
        """上(奥)を向く."""
        self.__tile_x, self.__tile_y = self.__tile_coordi_up
        self.__current_location_y -= self.__move_pixel

    def look_right(self):
        """右を向く."""
        self.__tile_x, self.__tile_y = self.__tile_coordi_right
        self.__current_location_x += self.__move_pixel

    def look_down(self):
        """下(手前)を向く."""
        self.__tile_x, self.__tile_y = self.__tile_coordi_down
        self.__current_location_y += self.__move_pixel

    def look_left(self):
        """左を向く."""
        self.__tile_x, self.__tile_y = self.__tile_coordi_left
        self.__current_location_x -= self.__move_pixel

    def get_tile_x(self):
        """X座標を返すGetter."""
        return self.__tile_x

    def get_tile_y(self):
        """Y座標を返すGetter."""
        return self.__tile_y

    def get_current_location_x(self):
        """X座標を返すGetter."""
        return self.__current_location_x

    def get_current_location_y(self):
        """Y座標を返すGetter."""
        return self.__current_location_y


if __name__ == "__main__":
    dh = DrawHuman()
    print(dh.get_tile_x())
    print(dh.get_tile_y())

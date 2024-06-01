if __name__ == "__main__":  # noqa
    from path_option import *

from game_option import Option as Op


class DrawMoveObject:
    """操作するキャラクターの描画する座標を管理するクラス."""

    def __init__(self,
                 tile_coordi_up: list,
                 tile_coordi_right: list,
                 tile_coordi_down: list,
                 tile_coordi_left: list,
                 tile_x: int,
                 tile_y: int,
                 move_pixel: int):
        # Objectが描かれているタイル上の座標
        self.__tile_coordi_up = tile_coordi_up
        self.__tile_coordi_right = tile_coordi_right
        self.__tile_coordi_down = tile_coordi_down
        self.__tile_coordi_left = tile_coordi_left

        # 表示するタイル座標
        self.__tile_x = tile_x
        self.__tile_y = tile_y
        
        # 最初の場所からの移動したpixel
        self.__current_location_x = 0
        self.__current_location_y = 0

        # 移動pixel
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

    @property
    def get_tile_x(self):
        """X座標を返すGetter."""
        return self.__tile_x

    @property
    def get_tile_y(self):
        """Y座標を返すGetter."""
        return self.__tile_y

    @property
    def get_current_location_x(self):
        """X座標を返すGetter."""
        return self.__current_location_x

    @property
    def get_current_location_y(self):
        """Y座標を返すGetter."""
        return self.__current_location_y

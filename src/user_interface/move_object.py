from user_interface.direction import Direction
from game_option import Option as Op


class MoveObject:
    """操作するキャラクターの描画する座標を管理するクラス."""

    def __init__(self,
                 tile_coordi_top: list,
                 tile_coordi_right: list,
                 tile_coordi_bottom: list,
                 tile_coordi_left: list,
                 first_direction: int,
                 tile_size_x: int,
                 tile_size_y: int,
                 first_location_x: int,
                 first_location_y: int,
                 move_pixel: int,
                 max_hp: int):
        """
        Args:
            tile_coordi_top: 奥向きのオブジェクトのタイル座標
            tile_coordi_right: 右向きのオブジェクトのタイル座標
            tile_coordi_bottom: 手前向きのオブジェクトのタイル座標
            tile_coordi_left: 左向きのオブジェクトのタイル座標
            first_direction: int,
            tile_size_x: int = 16,
            tile_size_y: int = 16,
            first_location_x: int = 0,
            first_location_y: int = 0,
            move_pixel: 移動速度
        """
        # Objectが描かれているタイル上の座標
        self.__tile_coordi_top = tile_coordi_top
        self.__tile_coordi_right = tile_coordi_right
        self.__tile_coordi_bottom = tile_coordi_bottom
        self.__tile_coordi_left = tile_coordi_left

        # オブジェクトの向く方向を管理する変数(Directionのvalue)
        self.__now_tile_coordi = None
        self.update_direction(first_direction)

        # タイルサイズ
        self.__tile_size_x = tile_size_x
        self.__tile_size_y = tile_size_y

        # 移動pixel
        self.__move_pixel = move_pixel

        # 最初の場所からの移動したpixel
        self.__current_location_x = first_location_x
        self.__current_location_y = first_location_y

        # HPゲージの作成
        self.__max_hp = max_hp
        self.__current_hp = max_hp

    def update_direction(self, dirction: int):
        """オブジェクトの表示タイル更新関数.
        オブジェクトの向きによって表示するタイル座標を変更.
        """
        if dirction == Direction.UP.value:
            self.__now_tile_coordi = self.__tile_coordi_top
        elif dirction == Direction.RIGHT.value:
            self.__now_tile_coordi = self.__tile_coordi_right
        elif dirction == Direction.DOWN.value:
            self.__now_tile_coordi = self.__tile_coordi_bottom
        elif dirction == Direction.LEFT.value:
            self.__now_tile_coordi = self.__tile_coordi_left

    def move_object(self, dirction: int):
        """オブジェクト座標更新関数."""
        if dirction == Direction.UP.value:
            if (self.__current_location_y - self.__move_pixel) >= 0:
                # マップ内にいれば座標を更新
                self.__current_location_y -= self.__move_pixel

        elif dirction == Direction.RIGHT.value:
            if (self.__current_location_x + self.__move_pixel) <= (Op.window_w - self.__tile_size_x):
                # マップ内にいれば座標を更新
                self.__current_location_x += self.__move_pixel

        elif dirction == Direction.DOWN.value:
            if (self.__current_location_y + self.__move_pixel) <= (Op.window_h - self.__tile_size_y):
                # マップ内にいれば座標を更新
                self.__current_location_y += self.__move_pixel

        elif dirction == Direction.LEFT.value:
            if (self.__current_location_x - self.__move_pixel) >= 0:
                # マップ内にいれば座標を更新
                self.__current_location_x -= self.__move_pixel

    def update_hp(self, add_hp):
        """HPの値を変更する関数.
        減らす場合は負の値を受け取る
        """
        self.__current_hp += add_hp

    @property
    def get_tile_coordi_x(self):
        """オブジェクトのタイルマップ上x座標返すGetter."""
        return self.__now_tile_coordi[0]

    @property
    def get_tile_coordi_y(self):
        """オブジェクトのタイルマップ上y座標返すGetter."""
        return self.__now_tile_coordi[1]

    @property
    def get_tile_size_x(self):
        """タイルサイズxを返すGetter."""
        return self.__tile_size_x

    @property
    def get_tile_size_y(self):
        """タイルサイズyを返すGetter."""
        return self.__tile_size_y

    @property
    def get_current_location_x(self):
        """現在座標xを返すGetter."""
        return self.__current_location_x

    @property
    def get_current_location_y(self):
        """現在座標yを返すGetter."""
        return self.__current_location_y

    @property
    def get_hp_current(self):
        """現在のHP返すGetter."""
        return self.__current_hp

    @property
    def get_hp_max(self):
        """現在のHP返すGetter."""
        return self.__max_hp

    @property
    def get_chara_size_x(self):
        """キャラクターのXサイズを返すGetter."""
        return self.__tile_size_x

    @property
    def get_chara_size_y(self):
        """キャラクターのXサイズを返すGetter."""
        return self.__tile_size_y

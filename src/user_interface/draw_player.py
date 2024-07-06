import os
import json

from user_interface.draw_move_object import DrawMoveObject

PROJECT_PATH = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
JSON_PATH = os.path.join(PROJECT_PATH, "resources",
                         "charactors", "players.json")


class DrawPlayer(DrawMoveObject):
    """操作するキャラクターの描画する座標を管理するクラス."""

    def __init__(self, chara_name,
                 first_location_x, first_location_y, first_direction):

        with open(JSON_PATH, 'r') as f:
            data = json.load(f)

        self.player_info = data.get(chara_name)

        # コンストラクタ
        super().__init__(
            tile_coordi_top=self.player_info["coordi_top"],
            tile_coordi_right=self.player_info["coordi_right"],
            tile_coordi_bottom=self.player_info["coordi_bottom"],
            tile_coordi_left=self.player_info["coordi_left"],
            first_direction=first_direction,
            tile_size_x=self.player_info["size_x"],
            tile_size_y=self.player_info["size_y"],
            first_location_x=first_location_x,
            first_location_y=first_location_y,
            move_pixel=self.player_info["spd"],
            max_hp=self.player_info["hp_max"]
        )

    @property
    def get_chara_size_x(self):
        """キャラクターのXサイズを返すGetter."""
        return self.player_info["size_x"]

    @property
    def get_chara_size_y(self):
        """キャラクターのXサイズを返すGetter."""
        return self.player_info["size_y"]

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

        player_info = data.get(chara_name)

        # コンストラクタ
        super().__init__(
            tile_coordi_top=player_info["coordi_top"],
            tile_coordi_right=player_info["coordi_right"],
            tile_coordi_bottom=player_info["coordi_bottom"],
            tile_coordi_left=player_info["coordi_left"],
            first_direction=first_direction,
            tile_size_x=player_info["size_x"],
            tile_size_y=player_info["size_y"],
            first_location_x=first_location_x,
            first_location_y=first_location_y,
            move_pixel=player_info["spd"],
            max_hp=player_info["hp_max"]
        )

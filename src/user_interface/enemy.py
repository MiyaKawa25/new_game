import os
import yaml

from user_interface.move_object import MoveObject

PROJECT_PATH = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
YAML_PATH = os.path.join(PROJECT_PATH, "resources",
                         "charactors", "enemies.yaml")


class Enemy(MoveObject):
    """操作するキャラクターの描画する座標を管理するクラス."""

    def __init__(self, enemy_name,
                 first_location_x, first_location_y, first_direction):

        with open(YAML_PATH, 'r') as f:
            data = yaml.safe_load(f)

        enemy_info = data[enemy_name]

        # コンストラクタ
        super().__init__(
            tile_coordi_top=enemy_info["coordi_top"],
            tile_coordi_right=enemy_info["coordi_right"],
            tile_coordi_bottom=enemy_info["coordi_bottom"],
            tile_coordi_left=enemy_info["coordi_left"],
            first_direction=first_direction,
            tile_size_x=enemy_info["size_x"],
            tile_size_y=enemy_info["size_y"],
            first_location_x=first_location_x,
            first_location_y=first_location_y,
            move_pixel=enemy_info["spd"],
            max_hp=enemy_info["hp_max"]
        )

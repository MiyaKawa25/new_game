import pyxel
import os
import yaml
from user_interface.tile_map import TileMap
from scenes.scene import Scene
from game_option import Option as Op
from user_interface.player import Player
from user_interface.enemy import Enemy
from user_interface.direction import Direction

PROJECT_PATH = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STAGE_YAML_PATH = os.path.join(
    PROJECT_PATH, "resources", "stage", "stage01.yaml")


class TestScene(Scene):
    def __init__(self):
        super().__init__()

        # 画像関連
        TileMap.set_map("sample.pyxres")

        self.player = None
        self.enemy_list = [] # enemyのインスタンスを格納していく

        # 実行しているシーンを見極めるための変数
        self.execute_scene_name = "Testscene"

        self.create_object()

    def create_object(self):
        """キャラクターオブジェクトを生成する関数."""
        with open(STAGE_YAML_PATH, 'r') as f:
            character_info = yaml.safe_load(f)

        # Player
        player_info = character_info["Player"]
        self.player = Player(chara_name=player_info["name"],
                                        first_location_x=player_info["location_x"],
                                        first_location_y=player_info["location_y"],
                                        first_direction=Direction[player_info["direction"]].value)

        # Enemy
        # Jsonファイルに記述しているキャラのインスタンスを生成
        for key, value in character_info.items():
            if key == "Player":
                continue
            object = Enemy(
                enemy_name=value["name"],
                first_location_x=value["location_x"],
                first_location_y=value["location_y"],
                first_direction=Direction[value["direction"]].value)
            self.enemy_list.append(object)

    def update(self):
        """ゲームの状態を更新する."""
        direction_id = None  # Keyが押されたかの判断
        
        if pyxel.btn(pyxel.KEY_UP):
            direction_id = Direction.UP.value
        elif pyxel.btn(pyxel.KEY_RIGHT):
            direction_id = Direction.RIGHT.value
        elif pyxel.btn(pyxel.KEY_DOWN):
            direction_id = Direction.DOWN.value
        elif pyxel.btn(pyxel.KEY_LEFT):
            direction_id = Direction.LEFT.value

        if direction_id is not None:
            self.player.update_direction(direction_id)
            self.player.move_object(direction_id)

    def draw(self):
        """描画を行う関数.
        画像の描画
        pyxel.blt(描画位置x, 描画位置y, 画像ID,
                  描画元画像x, 描画元画像y, 描画幅, 描画高さ, 色)
        """
        pyxel.cls(0)

        # 背景
        pyxel.bltm(0, 0, 0, 0, 0, Op.window_w, Op.window_h)

        # 操作キャラ
        self.draw_object(self.player)
        self.draw_object_hp(self.player)

        # 複数の敵を表示
        for enemy in self.enemy_list:
            self.draw_object(enemy)
            self.draw_object_hp(enemy)

    def next_scene(self):
        """次のシーンを返すメソッド."""
        return None

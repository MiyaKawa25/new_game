import pyxel
import os
import json
from user_interface.tile_map import TileMap
from scenes.scene import Scene
from game_option import Option as Op
from user_interface.draw_player import DrawPlayer
from user_interface.draw_enemy import DrawEnemy
from user_interface.direction import Direction

PROJECT_PATH = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STAGE_JSON_PATH = os.path.join(
    PROJECT_PATH, "resources", "stage", "stage01.json")


class TestScene(Scene):

    ENEMY_LIST = ["Sheep"]
    ENEMY_NUM_LIST = [2]

    def __init__(self):
        super().__init__()

        self.player_list = ["Slime"]
        self.enemy_list = TestScene.ENEMY_LIST

        # 画像関連
        TileMap.set_map("sample.pyxres")

        self.control_character = None
        self.enemy_object_list = []

        # 実行しているシーンを見極めるための変数
        self.execute_scene_name = "Testscene"

        self.create_object()

    def create_object(self):
        """キャラクターオブジェクトを生成する関数."""
        with open(STAGE_JSON_PATH, 'r') as f:
            character_info = json.load(f)

        # Player
        player = character_info["Player"]
        self.control_character = DrawPlayer(chara_name=player["name"],
                                            # 中心
                                            first_location_x=player["location_x"],
                                            # 中心
                                            first_location_y=player["location_y"],
                                            first_direction=getattr(Direction, player["direction"]).value)

        # Enemy
        # Jsonファイルに記述しているキャラのインスタンスを生成
        for key, value in character_info.items():
            if key == "Player":
                continue
            object = DrawEnemy(
                enemy_name=value["name"],
                first_location_x=value["location_x"],
                first_location_y=value["location_y"],
                first_direction=getattr(Direction, value["direction"]).value)
            self.enemy_object_list.append(object)

    def update(self):
        """ゲームの状態を更新する."""
        push_key_flag = None  # Keyが押されたかの判断
        if pyxel.btn(pyxel.KEY_UP):
            push_key_flag = Direction.UP.value
        elif pyxel.btn(pyxel.KEY_RIGHT):
            push_key_flag = Direction.RIGHT.value
        elif pyxel.btn(pyxel.KEY_DOWN):
            push_key_flag = Direction.DOWN.value
        elif pyxel.btn(pyxel.KEY_LEFT):
            push_key_flag = Direction.LEFT.value

        if push_key_flag is not None:
            self.control_character.update_direction(push_key_flag)
            self.control_character.move_object(push_key_flag)

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
        self.draw_object(self.control_character)
        self.draw_object_hp(self.control_character)

        # 複数の敵を表示
        for enemy in self.enemy_object_list:
            self.draw_object(enemy)
            self.draw_object_hp(enemy)

    def draw_object(self, object):
        """オブジェクト描画用関数.
        """
        # オブジェクトの表示
        pyxel.bltm(object.get_current_location_x,
                   object.get_current_location_y,
                   0,
                   object.get_tile_coordi_x, object.get_tile_coordi_y,
                   object.get_tile_size_x, object.get_tile_size_y,
                   0)

    def draw_object_hp(self, object):
        """オブジェクトのHPゲージを描画する関数.
        pyxel.rect(左上x, 左上y, x幅, y幅, カラー)

        # パレットカラー
            https://note.com/syun77/n/nf0f094854644#:~:text=%E3%83%91%E3%83%AC%E3%83%83%E3%83%88%E3%82%AB%E3%83%A9%E3%83%BC%E3%81%AF%E4%BB%A5%E4%B8%8B%E3%81%AE%E3%82%82%E3%81%AE%E3%81%8C%E7%94%A8%E6%84%8F%E3%81%95%E3%82%8C%E3%81%A6%E3%81%84%E3%81%BE%E3%81%99%E3%80%82
        """
        # HPゲージの表示
        height_hp = 4
        # 白(HPゲージ外枠)
        pyxel.rect(object.get_current_location_x,
                   object.get_current_location_y+object.get_chara_size_y,
                   object.get_chara_size_x,
                   height_hp,
                   7)
        # 黒(減HPを表す色)
        hp_gauge_wide_max = object.get_chara_size_x - 2
        pyxel.rect(object.get_current_location_x + 1,
                   object.get_current_location_y+object.get_chara_size_y + 1,
                   hp_gauge_wide_max,
                   height_hp-2,
                   0)
        # 青(残HPを表す色)
        hp_gauge_wide_current = int(
            hp_gauge_wide_max * (object.get_hp_current / object.get_hp_max))
        pyxel.rect(object.get_current_location_x + 1,
                   object.get_current_location_y+object.get_chara_size_y + 1,
                   hp_gauge_wide_current,
                   height_hp-2,
                   12)

    def next_scene(self):
        """次のシーンを返すメソッド."""
        return None

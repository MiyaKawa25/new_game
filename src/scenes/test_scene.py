import pyxel
if __name__ == "__main__":  # noqa
    from path_option import *
from user_interface.tile_map import TileMap
from scenes.scene import Scene
from game_option import Option as Op
from user_interface.draw_human import DrawHuman
from user_interface.draw_slime import DrawSlime
from user_interface.draw_enemy import DrawEnemy
from user_interface.direction import Direction


class TestScene(Scene):
    def __init__(self):
        super().__init__()

        # 画像関連
        TileMap.set_map("sample.pyxres")
        self.control_character = DrawSlime(first_location_x=(Op.window_w//2)-8,  # 中心
                                           first_location_y=(Op.window_h//2)-8,  # 中心
                                           first_direction=Direction.DOWN.value,
                                           move_pixel=2)
        self.enemy1 = DrawEnemy(first_location_x=(Op.window_w//4)-8,
                                first_location_y=(Op.window_h//4)-8,
                                first_direction=Direction.DOWN.value,
                                move_pixel=2)
        # 実行しているシーンを見極めるための変数
        self.execute_scene_name = "Testscene"

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

        # 敵1
        self.draw_object(self.enemy1)

    def draw_object(self, draw_object):
        """オブジェクト描画用関数."""
        pyxel.bltm(draw_object.get_current_location_x,
                   draw_object.get_current_location_y,
                   0,
                   draw_object.get_tile_coordi_x, draw_object.get_tile_coordi_y,
                   draw_object.get_tile_size_x, draw_object.get_tile_size_y,
                   0)

    def next_scene(self):
        """次のシーンを返すメソッド."""
        return None


if __name__ == "__main__":
    pyxel.init(Op.window_w, Op.window_h)  # (W, H)
    map_scene = TestScene()
    map_scene.update_flame()

import pyxel
if __name__ == "__main__":  # noqa
    from path_option import *
from user_interface.tile_map import TileMap
from scenes.scene import Scene
from game_option import Option as Op
from user_interface.draw_human import DrawHuman


class TestScene(Scene):
    def __init__(self):
        super().__init__()

        # 画像関連
        TileMap.set_map("sample.pyxres")
        self.human = DrawHuman()

        # 実行しているシーンを見極めるための変数
        self.execute_scene_name = "Testscene"

    def update(self):
        """ゲームの状態を更新する."""
        # 決定ボタン(SPACE)
        if pyxel.btn(pyxel.KEY_UP):
            self.human.look_up()
            self.human.move_up()
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.human.look_right()
            self.human.move_right()
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.human.look_down()
            self.human.move_down()
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.human.look_left()
            self.human.move_left()

    def draw(self):
        """描画を行う関数.
        画像の描画
        pyxel.blt(描画位置x, 描画位置y, 画像ID,
                  描画元画像x, 描画元画像y, 描画幅, 描画高さ, 色)
        """
        pyxel.cls(0)

        # 背景
        pyxel.bltm(0, 0, 0, 0, 0, Op.window_w, Op.window_h)

        # キャラクター
        pyxel.bltm((Op.window_w//2)-8+self.human.get_current_location_x,
                   (Op.window_h//2)-8+self.human.get_current_location_y,
                   0,
                   self.human.get_tile_x, self.human.get_tile_y,
                   16, 16, 0)

    def next_scene(self):
        """次のシーンを返すメソッド."""
        return None


if __name__ == "__main__":
    pyxel.init(Op.window_w, Op.window_h)  # (W, H)
    map_scene = TestScene()
    map_scene.update_flame()

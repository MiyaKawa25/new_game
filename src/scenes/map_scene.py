import pyxel
if __name__ == "__main__":  # noqa
    from path_option import *
from user_interface.image_manager import ImageManager
from scenes.scene import Scene


class MapScene(Scene):
    def __init__(self):
        super().__init__()

        # 画像関連
        ImageManager.set_img_background("story_240_180.png")

        # 実行しているシーンを見極めるための変数
        self.execute_scene_name = "MapScene"

        # テキストボックスフラグ
        self.text_box_flag = False

    def update(self):
        """ゲームの状態を更新する."""
        # 決定ボタン(SPACE)
        if pyxel.btnp(pyxel.KEY_SPACE):  # pyxel.KEY_ENTERは使えない
            self.text_box_flag = not self.text_box_flag

    def draw(self):
        """描画を行う関数.
        画像の描画
        pyxel.blt(描画位置x, 描画位置y, 画像ID,
                  描画元画像x, 描画元画像y, 描画幅, 描画高さ, 色)
        """
        # pyxel.cls(0)  # 画面クリア
        pyxel.blt(0, 0, ImageManager.background_index(),
                  0, 0, pyxel.width, pyxel.height)  # 背景
        if self.text_box_flag:
            self.message.show_text_box()

    def next_scene(self):
        """次のシーンを返すメソッド."""
        return None


if __name__ == "__main__":
    pyxel.init(240, 180)  # (W, H)
    map_scene = MapScene()
    map_scene.update_flame()

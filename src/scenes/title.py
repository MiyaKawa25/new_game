import pyxel
if __name__ == "__main__":  # noqa
    from path_option import *
from scenes.scene import Scene
from scenes.map_scene import MapScene
from user_interface.image_manager import ImageManager
from user_interface.calculator import Calculator


class TitleScene(Scene):

    def __init__(self):
        super().__init__()

        # 画像関連
        ImageManager.set_img_background("title_background_240_180.png")

        # タイトル関連
        self.game_title = "TITLE"
        self.title_font_size = 30

        # メニュー関連
        self.title_menu = ["つづきから", "はじめから"]
        self.select_font_size = 15
        self.select_menu_index = 0

        # 実行しているシーンを見極めるための変数
        self.execute_scene_name = "Title"

    def update(self):
        """ゲームの状態を更新する."""
        # ↑↓ボタン関連の更新
        if pyxel.btnp(pyxel.KEY_UP):
            self.select_menu_index += 1
        elif pyxel.btnp(pyxel.KEY_DOWN):
            self.select_menu_index -= 1
        # 文字列リセット
        self.changed_title_menu = self.title_menu.copy()
        # インデックス正規化
        self.select_menu_index %= len(self.changed_title_menu)
        # "→"の付与
        self.changed_title_menu[self.select_menu_index] = "→ " + \
            self.changed_title_menu[self.select_menu_index]

        # 決定ボタン(SPACE)
        if pyxel.btnp(pyxel.KEY_SPACE):  # pyxel.KEY_ENTERは使えない
            self.game_running = False

    def draw(self):
        """描画を行う関数.
        画像の描画
        pyxel.blt(描画位置x, 描画位置y, 画像ID,
                  描画元画像x, 描画元画像y, 描画幅, 描画高さ, 色)
        """
        # pyxel.cls(0)  # 画面クリア
        pyxel.blt(0, 0, ImageManager.background_index(),
                  0, 0, pyxel.width, pyxel.height)  # 背景

        # タイトルが中心に来るように計算
        x = Calculator.calc_text_x(self.game_title, 30)

        # タイトル表示
        self.writer.draw(int(x), 50, self.game_title, self.title_font_size, 1)

        # セレクトボタンの表示
        y = 100
        for button in self.changed_title_menu:
            x = Calculator.calc_text_x(button, 20)
            self.writer.draw(int(x), y, button, self.select_font_size, 1)
            y += 30

    def next_scene(self):
        """次のシーンを返すメソッド."""
        return MapScene()


if __name__ == "__main__":
    pyxel.init(240, 180)  # (W, H)
    title = Title()
    title.update_flame()

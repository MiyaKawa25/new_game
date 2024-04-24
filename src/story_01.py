import pyxel

from game_option import Option as Op
from game import Game


class Story01(Game):
    def __init__(self):
        super().__init__()

        # ゲーム素材の読み込み
        self.read_data()

        # ゲーム続行フラグ
        self.game_running = True

        # テキストボックスフラグ
        self.text_box_flag = False

        # ゲーム開始
        self.run()

    def run(self):
        while self.game_running:
            self.update()
            self.draw()
            pyxel.flip()  # フレームを更新

    def read_data(self):
        """必要データの読み来み."""
        self.bkg_story01_index = self.read_img_data(Op.bkg_story01)

    def update(self):
        """ゲームの状態を更新する."""
        if pyxel.btnp(pyxel.KEY_SPACE):  # pyxel.KEY_ENTERは使えない
            self.text_box_flag = not self.text_box_flag

    def draw(self):
        """描画を行う関数.
        画像の描画
        pyxel.blt(描画位置x, 描画位置y, 画像ID,
                  描画元画像x, 描画元画像y, 描画幅, 描画高さ, 色)
        """
        pyxel.blt(0, 0, self.bkg_story01_index, 0, 0,
                  pyxel.width, pyxel.height)  # 背景
        self.writer.draw(pyxel.width/3, 50, "ストーリー０１", 20, 1)  # 文字

        if self.text_box_flag:
            self.show_text_box()


if __name__ == "__main__":
    pyxel.init(Op.WINDOW_W, Op.WINDOW_H)  # (W, H)
    Story01()

import pyxel

from game_option import Option as Op
from game import Game


class Title(Game):
    def __init__(self):
        super().__init__()

        # ゲーム素材の読み込み
        self.read_data()

        # 初回読み込みフラグ
        self.is_initialized = True

        # 選択しているボタン番号
        self.selct_button_index = 0

        # ゲーム続行フラグ
        self.game_running = True

        # ゲーム開始
        self.run()

    def run(self):
        while self.game_running:
            self.update()
            self.draw()
            pyxel.flip()  # フレームを更新

    def read_data(self):
        """必要データの読み込み."""
        # 画像
        self.bkg_title_index = self.read_img_data(Op.bkg_title)
        # ボタン
        self.title_button = None
        # self.title_button = Op.title_button.copy()

    def update(self):
        """ゲームの状態を更新する."""
        # ↑↓ボタン関連の更新
        if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.KEY_DOWN) \
                or self.is_initialized:
            self.is_initialized = False
            if pyxel.btnp(pyxel.KEY_UP):
                self.selct_button_index += 1
            elif pyxel.btnp(pyxel.KEY_DOWN):
                self.selct_button_index -= 1
            self.title_button = Op.title_button.copy()  # 文字列リセット
            self.selct_button_index %= len(self.title_button)
            self.title_button[self.selct_button_index] = "→ " + \
                self.title_button[self.selct_button_index]

        # 決定ボタン(SPACE)
        if pyxel.btnp(pyxel.KEY_SPACE):  # pyxel.KEY_ENTERは使えない
            self.game_running = False

    def draw(self):
        """描画を行う関数.
        画像の描画
        pyxel.blt(描画位置x, 描画位置y, 画像ID,
                  描画元画像x, 描画元画像y, 描画幅, 描画高さ, 色)
        """
        pyxel.cls(0)  # 画面クリア
        pyxel.blt(0, 0, self.bkg_title_index,
                  0, 0, pyxel.width, pyxel.height)  # 背景

        # タイトルが中心に来るように計算
        x = self.calu_text_x(Op.game_title, 30)
        # タイトル表示
        self.writer.draw(int(x), 50, Op.game_title, Op.title_font_size, 1)

        # セレクトボタンの表示
        y = 100
        for button in self.title_button:
            x = self.calu_text_x(button, 20)
            self.writer.draw(int(x), y, button, Op.select_font_size, 1)
            y += 30


if __name__ == "__main__":
    pyxel.init(Op.WINDOW_W, Op.WINDOW_H)  # (W, H)
    Title()

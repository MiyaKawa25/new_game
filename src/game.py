import pyxel
import os
import PyxelUniversalFont as puf

from game_option import Option as Op


class Game:
    """ゲームクラス(親)."""
    # 初回呼び出しを判断する変数
    is_initialized = True

    def __init__(self):
        if Game.is_initialized:
            # ゲームウィンドウの作成
            pyxel.init(Op.WINDOW_W, Op.WINDOW_H)  # (W, H)
            Game.is_initialized = False

        # フォントを指定
        self.writer = puf.Writer("misaki_gothic.ttf")

        # 画像番号を割り振るための変数
        self.count_img_index = 0

        # 画像データの読み込み
        self.text_box_img_index = self.read_img_data(Op.text_box_img)

    def read_img_data(self, img_name):
        """画像ファイルをPyxelで読み込む関数.
        Args:
            img_name(str): 画像ファイル名
        Return:
            int: 画像識別番号(index)
        """
        self.count_img_index += 1
        path = os.path.join(Op.data_dir, img_name)
        if not os.path.exists(path):
            raise FileNotFoundError(f"File does not exist: {path}")
        pyxel.images[self.count_img_index].load(0, 0, path)
        return self.count_img_index

    def show_text_box(self):
        """テキストボックスの表示.
        pyxel.blt(描画位置x, 描画位置y, 画像ID,
            描画元画像x, 描画元画像y, 描画幅, 描画高さ, 色)
        """
        pyxel.blt(0, pyxel.height-48, self.text_box_img_index,
                  0, 0, pyxel.width, 48)

    def calu_text_size(self, text):
        """文字数カウント関数.
        全角を1, アルファベットを0.5でカウントする。
        Args:
            text(str): カウントする文字列
        """
        count = 0
        for t in text:
            # 全角の場合
            if (0x3000 <= ord(t) <= 0x9FFF) \
                    or (0xFF00 <= ord(t) <= 0xFFEF):
                count += 1
            # アルファベットの場合
            elif (0x41 <= ord(t) <= 0x5A) \
                    or (0x61 <= ord(t) <= 0x7A):
                count += 0.5
            else:  # TODO:アルファベットと合わせてもいい？
                count += 0.5
        return count

    def calu_text_x(self, text, font_size):
        """テキストを画面中心に配置する際のx座標を求める関数.
        Args:
            text(str): テキスト
            font_size(int): テキストのフォントサイズ

        Return:
            double: テキストが画面中心にくるためのx座標
        """
        adjustment = 4
        text_size = self.calu_text_size(text)
        return (pyxel.width - (font_size * text_size)) / 2 + adjustment


if __name__ == "__main__":
    pyxel.init(Op.WINDOW_W, Op.WINDOW_H)  # (W, H)
    Game()

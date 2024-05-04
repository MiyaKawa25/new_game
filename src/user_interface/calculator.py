import pyxel


class Calculator:
    @staticmethod
    def calc_text_size(text):
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

    @staticmethod
    def calc_text_x(text, font_size):
        """テキストを画面中心に配置する際のx座標を求める関数.
        Args:
            text(str): テキスト
            font_size(int): テキストのフォントサイズ

        Return:
            double: テキストが画面中心にくるためのx座標
        """
        adjustment = 4
        text_size = Calculator.calc_text_size(text)
        return (pyxel.width - (font_size * text_size)) / 2 + adjustment

import pyxel
from user_interface.image_manager import ImageManager


class Message:
    def __init__(self):
        ImageManager.set_img_text_box("text_box_240_48.png")

    def show_text_box(self):
        """テキストボックスの表示.
        pyxel.blt(描画位置x, 描画位置y, 画像ID,
            描画元画像x, 描画元画像y, 描画幅, 描画高さ, 色)
        """
        pyxel.blt(0, pyxel.height-48, ImageManager.text_box_index(),
                  0, 0, pyxel.width, 48)

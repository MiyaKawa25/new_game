import pyxel
import os

CURRENT_DIR_PATH = os.path.dirname(
    os.path.abspath(__file__))  # user_interface/
PROJECT_DIR_PATH = os.path.dirname(
    os.path.dirname(CURRENT_DIR_PATH))  # new_game


class ImageManager():
    """
    NOTE:pyxel.imagesは合計3枚の画像しか保持できない
    https://github.com/kitao/pyxel/blob/main/docs/README.ja.md
    よってとする
    0: 背景画像
    1: テキストボックス
    2: いろいろ
    """
    _resource_path = os.path.join(PROJECT_DIR_PATH, "resources")
    _background_index = 0
    _text_box_index = 1
    _other_index = 2

    @staticmethod
    def __load_img(path, index):
        """画像ファイルをPyxelで読み込む関数.
        Args:
            path(str): 画像のあるディレクトリパス
            img_name(str): 画像ファイル名
        """
        if not os.path.exists(path):
            raise FileNotFoundError(f"File does not exist: {path}")
        pyxel.images[index].load(0, 0, path)

    @classmethod
    def set_img_background(cls, img_name):
        """画像読み込みメソッド"""
        path = os.path.join(cls._resource_path, "worlds", "maps", img_name)
        cls.__load_img(path, cls._background_index)

    @classmethod
    def set_img_text_box(cls, img_name):
        """画像読み込みメソッド"""
        path = os.path.join(cls._resource_path, "interfaces", img_name)
        cls.__load_img(path, cls._background_index)

    @classmethod
    def set_img_other(cls):
        """画像読み込みメソッド
        未定義
        """
        pass

    @classmethod
    def background_index(cls):
        """インデックスを返すメソッド.
        Return:
            int: 背景画像のインデックス
        """
        # return 0
        return cls._background_index

    @classmethod
    def text_box_index(cls):
        """インデックスを返すメソッド.
        Return:
            int: テキストボックスのインデックス
        """
        return cls._text_box_index

    @classmethod
    def other_index(cls):
        """インデックスを返すメソッド.
        未定義
        Return:
            int: 他のインデックス
        """
        pass

import pyxel
from game_title import Title
from story_01 import Story01
from game_option import Option as Op


class Main:
    """ゲームクラス."""

    def __init__(self):
        self.run()

    def run(self):
        Title()
        Story01()


if __name__ == "__main__":
    Main()

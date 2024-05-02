import pyxel
from scenes.title import Title


class Game:
    def __init__(self):
        pyxel.init(240, 180)  # (W, H)
        self.play()

    def play(self):
        """シーンを再生するメソッド."""
        self.current_scene = Title()
        while self.current_scene is not None:
            # シーン
            self.current_scene.update_flame()

            # シーンの更新
            self.current_scene = self.current_scene.next_scene()


if __name__ == "__main__":
    Game()

import pyxel
from scenes.title_scene import TitleScene


class Game:
    def __init__(self):
        pyxel.init(240, 180)  # (W, H)
        self.play()

    def play(self):
        """シーンを再生するメソッド."""
        # 初期シーンのインスタンス化
        self.current_scene = TitleScene()
        while self.current_scene is not None:
            # シーン再生
            self.current_scene.update_flame()
            # 次のシーンのインスタンス化
            self.current_scene = self.current_scene.next_scene()


if __name__ == "__main__":
    Game()

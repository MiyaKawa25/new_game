import pyxel
from scenes.title_scene import TitleScene
from game_option import Option as Op


class Game:
    def __init__(self):
        pyxel.init(Op.window_w, Op.window_h)
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

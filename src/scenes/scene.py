import pyxel
import PyxelUniversalFont as puf
from user_interface.message import Message  # noqa


class Scene:
    # Sceneクラスをそのままインスタンス化しない
    # 今のところ、以下の5つを想定中
    #  - TitleScene: ロード時にセーブファイルを読み込みパラメータに格納する
    #  - Map: 移動や会話イベント、メニューの操作、バトルへの移行、などを行う
    #         役割が多いため、メニュー画面は別のシーン扱いでもいいかもしれない
    #  - Battle: 戦闘を行い、勝った場合はMapに戻り、負けた場合はOverに遷移する
    #  - Over: ゲームオーバー画面。基本的にはタイトルに遷移する(コンティニューはなくてもいいかな)
    #  - End: エンドロールを流し、タイトル画面に遷移する
    is_initialized = True

    def __init__(self):
        """シーン初期化."""
        self.game_running = True  # シーン継続フラグ
        self.writer = puf.Writer("misaki_gothic.ttf")  # フォントを指定
        self.message = Message()
        self.execute_scene_name = "None"  # 作業用

    def update_flame(self):
        """フレーム更新メソッド."""
        print(f"実行シーン: {self.execute_scene_name}")
        while self.game_running:
            self.update()
            self.draw()
            pyxel.flip()  # フレームを更新

    def update(self):
        """オーバーライド前提メソッド."""
        pass

    def draw(self):
        """オーバーライド前提メソッド."""
        pass

    def next_scene(self):
        """オーバーライド前提メソッド.
        Return:
            次のシーンインスタンス
        """
        return None

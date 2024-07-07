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
        """オーバーライド前提メソッド.
        NOTE:
            # 長押し非対応
            pyxel.btnp(pyxel.KEY_UP)
            # 長押し対応
            pyxel.btn(pyxel.KEY_UP)
        """
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

    def draw_object(self, object):
        """オブジェクト描画用関数."""
        # オブジェクトの表示
        pyxel.bltm(object.get_current_location_x,
                   object.get_current_location_y,
                   0,
                   object.get_tile_coordi_x, object.get_tile_coordi_y,
                   object.get_tile_size_x, object.get_tile_size_y,
                   0)

    def draw_object_hp(self, object):
        """オブジェクトのHPゲージを描画する関数.
        pyxel.rect(左上x, 左上y, x幅, y幅, カラー)

        # パレットカラー
            https://note.com/syun77/n/nf0f094854644#:~:text=パレットカラーは以下のものが用意されています。
        """
        # HPゲージの表示
        height_hp = 4
        # 白(HPゲージ外枠)
        pyxel.rect(object.get_current_location_x,
                   object.get_current_location_y+object.get_chara_size_y,
                   object.get_chara_size_x,
                   height_hp,
                   7)
        # 黒(減HPを表す色)
        hp_gauge_wide_max = object.get_chara_size_x - 2
        pyxel.rect(object.get_current_location_x + 1,
                   object.get_current_location_y+object.get_chara_size_y + 1,
                   hp_gauge_wide_max,
                   height_hp-2,
                   0)
        # 青(残HPを表す色)
        hp_gauge_wide_current = int(
            hp_gauge_wide_max * (object.get_hp_current / object.get_hp_max))
        pyxel.rect(object.get_current_location_x + 1,
                   object.get_current_location_y+object.get_chara_size_y + 1,
                   hp_gauge_wide_current,
                   height_hp-2,
                   12)

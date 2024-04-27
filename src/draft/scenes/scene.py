class Scene:
    # Sceneクラスをそのままインスタンス化しない
    # 今のところ、以下の5つを想定中
    #  - TitleScene: ロード時にセーブファイルを読み込みパラメータに格納する
    #  - Map: 移動や会話イベント、メニューの操作、バトルへの移行、などを行う
    #         役割が多いため、メニュー画面は別のシーン扱いでもいいかもしれない
    #  - Battle: 戦闘を行い、勝った場合はMapに戻り、負けた場合はOverに遷移する
    #  - Over: ゲームオーバー画面。基本的にはタイトルに遷移する(コンティニューはなくてもいいかな)
    #  - End: エンドロールを流し、タイトル画面に遷移する
    params

    def __init__(self):
        # シーン初期化
        pass

    def update(self):
        # パラメータ更新
        pass

    def draw(self):
        # 描画
        pass

    def next_scene(self):
        # 次のシーンを返す
        # Sceneオブジェクトを返すのか、"map"や"battle"といった文字列を返すのかは要検討
        pass
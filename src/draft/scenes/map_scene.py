class MapScene(Scene):
    params

    def __init__(self):
        # 親クラスのコンストラクタ呼び出し
        pass

    def update(self):
        # 乱数でエンカウントフラグを立てる
        # キー入力用のクラスを通じて、ユーザの入力受付
            # WASDもしくは矢印キーの入力で移動
            # BackSpaceでメニューUIの表示・マップ移動不可にする
            # etc.
        pass

    def draw(self):
        pass

    def next_scene(self):
        # エンカウントフラグが立っていれば、BattleSceneに遷移
        pass
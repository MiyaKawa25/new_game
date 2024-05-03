from scene import Scene
from enum import Enum

class MapSceneState(Enum):
    TALK = 1
    MOVE = 2
    MENU = 3

class MapScene(Scene):
    def __init__(self):
        # 親クラスのコンストラクタ呼び出し
        super().__init__()
        # パラメータ初期化(本来はセーブデータを受け取り参照)
        params = {
            "state": MapSceneState.TALK,
            "story_id": 1,
            "story_action_id": 0,
        }

    def update(self, user_input):
        if self.params.state is :
            if user_input is not None:
                # セリフの表示
                pass
        elif False:
            # 乱数でエンカウントフラグを立てる
            pass
        elif user_input is not None:
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

    def __play_story(self):
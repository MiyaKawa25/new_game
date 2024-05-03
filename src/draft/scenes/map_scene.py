from scene import Scene
from enum import Enum
from yaml import safe_load

class MapSceneState(Enum):
    STORY = 1
    MOVE = 2
    MENU = 3

class MapScene(Scene):
    def __init__(self):
        # 親クラスのコンストラクタ呼び出し
        super().__init__()
        # パラメータ初期化(ToDo:セーブデータを受け取り参照)
        self.params = {
            "player_name": "オプティ",
            "story_id": "000_opening_event",
            "opening_event": True,
        }
        # シーン内で用いる値を初期化
        self.state = None
        self.story = None
        self.story_event_id = 0
        self.story_event = None
        self.blackout = False
        self.talker_id = None
        self.message_id = 0
        self.message_content = ""
        self.sound = None
        self.walker_id = None
        self.walk_speed = 0
        self.walk_route = None
        # ストーリーファイル読み込み
        with open(f"../resources/stories/{self.params['story_id']}.yaml") as f:
            self.story = safe_load(f)
        is_valid_story = True
        for param, expected in self.story["before"].items():
            if self.params[param] != expected:
                is_valid_story = False
                break
        if is_valid_story:
            self.state = MapSceneState.STORY
            self.story_event_id = 0
            self.story_event = self.story["events"][self.story_event_id]
        else:
            self.story = None

        # テスト用
        while True:
            print(f"*{self.story_event_id}************")
            print(self.story_event)
            self.update("a")
            self.draw()
            print("*************\n")


    def update(self, user_input):
        """パラメータの更新"""
        if self.state is MapSceneState.STORY:
            if user_input is not None:
                self.__carry_event()
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
        print("=============")
        if len(self.message_content) > 0:
            print(f"[talker_{self.talker_id}]: {self.message_content}")
        if self.sound is not None:
            print(self.sound)
        if self.blackout:
            print("BLACKOUT")

    def next_scene(self):
        # エンカウントフラグが立っていれば、BattleSceneに遷移
        pass

    def __carry_event(self):
        """イベントを進行する"""
        self.story_event = self.story["events"][self.story_event_id]
        # 暗転判定
        if "blackout" in self.story_event.keys():
            self.blackout = self.story_event["blackout"]
        # 会話の進行
        if "say" in self.story_event.keys():
            if self.message_id < len(self.story_event["say"]["messages"]):
                self.message_content = self.story_event["say"]["messages"][self.message_id]
                self.message_id += 1
                # メッセージを表示し終えない間は、イベントの進行をスキップする
                return
            else:
                # メッセージを表示しきった場合は初期化する
                self.talker_id = None
                self.message_id = 0
                self.message_content = ""                
        if "select" in self.story_event.keys():
            # 選択肢の選択を要求
            user_select = int(input(self.story_event["select"]))
            # ユーザ選択に応じて、遷移イベントを変更
            self.story_event["next_event_id"] = list(self.story_event["select"][user_select].values())[0]
            print(self.story_event)
        if "sound" in self.story_event.keys():
            self.sound = self.story_event["sound"]
        if "walk" in self.story_event.keys():
            self.walker_id = self.story_event["walk"]["walker_id"]
            self.walk_speed = self.story_event["walk"]["speed"]
            self.walk_route = self.story_event["walk"]["route"]

        # イベントの進行
        if "next_event_id" in self.story_event.keys():
            self.story_event_id = self.story_event["next_event_id"]
        else:
            self.story_event_id += 1

        if self.story_event_id in self.story["events"].keys():
            # イベントの初期化
            self.story_event = self.story["events"][self.story_event_id]
            if "say" in self.story_event.keys():
                self.talker_id = self.story_event["say"]["talker_id"]
            if "sound" not in self.story_event.keys():
                self.sound = None
        else:
            # イベント終了に応じてパラメータを更新する
            for param, new_value in self.story["after"].items():
                self.params[param] = new_value
            # 全てのイベントが終了した場合、移動可能状態に移行
            self.state = MapSceneState.MOVE
            self.story = None
            self.story_event_id = 0
            self.story_event = None
            self.blackout = False
            self.talker_id = None
            self.message_id = 0
            self.message_content = ""
            self.sound = None
            self.walker_id = None
            self.walk_speed = 0
            self.walk_route = None
if __name__ == "__main__":
    scene = MapScene()
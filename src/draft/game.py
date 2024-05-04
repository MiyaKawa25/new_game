class Game:
    current_scene: Scene = TitleScene()    # 現在のシーン。初期シーンはタイトル
    title: string
    params  # セーブデータに含める記憶すべきものと、ゲーム中にだけ必要なものは区別したい

    def play(self):
        ## 開始準備の処理 ##

        while self.params.is_playing:
            # ユーザの操作を取得
            user_input = ""
            # パラメータの更新
            self.params = self.current_scene.update(self.params, user_input)
            # 画面の描画
            self.current_scene.draw()
            # シーンの更新
            self.current_scene = self.current_scene.next_scene()

            ## 一定時間待機 ##

        ## 終了時の処理 ##

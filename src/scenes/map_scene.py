import pyxel
if __name__ == "__main__":  # noqa
    from path_option import *
from user_interface.tile_map import TileMap
from user_interface.image_manager import ImageManager
from scenes.scene import Scene
from game_option import Option as Op
from user_interface.draw_human import DrawHuman
from resources.maptrees.map_tree import MapTree
from resources.maptrees.sample_map_tree import sample_map_tree


class MapScene(Scene):
    def __init__(self):
        super().__init__()

        # 画像関連
        TileMap.set_map("sample.pyxres")
        self.human = DrawHuman(1)
        self.human.look_down()  # 下向きに固定

        # 実行しているシーンを見極めるための変数
        self.execute_scene_name = "MapScene"

        # テキストボックスフラグ
        self.text_box_flag = False

        # マップ情報
        self.map_tree = sample_map_tree
        self.current_map_node_id = 0

    def update(self):
        """ゲームの状態を更新する."""
        # 決定ボタン(SPACE)
        if pyxel.btnp(pyxel.KEY_SPACE):  # pyxel.KEY_ENTERは使えない
            self.text_box_flag = not self.text_box_flag
        # 矢印キー
        if pyxel.btnr(pyxel.KEY_UP):
            # 同じ親要素を持つ中で、現在のノードより上の中で、一番yが近いノードのIDを取得する
            self.current_map_node_id = self.map_tree.get_nearest_upper_sibling_node_id(self.current_map_node_id)
        elif pyxel.btnr(pyxel.KEY_RIGHT):
            # 子要素の中で、一番yが近いノードのIDを取得する
            self.current_map_node_id = self.map_tree.get_nearest_child_node_id(self.current_map_node_id)
        elif pyxel.btnr(pyxel.KEY_DOWN):
            # 同じ親要素を持つ中で、現在のノードより下の中で、一番yが近いノードのIDを取得する
            self.current_map_node_id = self.map_tree.get_nearest_lowwer_sibling_node_id(self.current_map_node_id)
        elif pyxel.btnr(pyxel.KEY_LEFT):
            # 親要素の中で、一番yが近いノードのIDを取得する
            self.current_map_node_id = self.map_tree.get_nearest_parent_node_id(self.current_map_node_id)


    def draw(self):
        """描画を行う関数.
        画像の描画
        pyxel.blt(描画位置x, 描画位置y, 画像ID,
                  描画元画像x, 描画元画像y, 描画幅, 描画高さ, 色)
        """
        pyxel.cls(0)  # 画面クリア

        # 背景
        pyxel.bltm(0, 0, 0, 0, 0, Op.window_w, Op.window_h)
        
        # マップ情報
        tail_length_w = Op.window_w // 32  # TODO: タイルマップの構造にそろえる
        tail_length_h = Op.window_h // 24  # TODO: タイルマップの構造にそろえる

        # ステージの表示
        for node in self.map_tree.nodes:
            # マップの道
            for child_id in node.children_ids:
                child_node = self.map_tree.nodes[child_id]
                pyxel.line(node.x * tail_length_w, node.y * tail_length_h,
                           child_node.x * tail_length_w, child_node.y * tail_length_h,
                           9)
            pyxel.blt(node.x * tail_length_w,
                      node.y * tail_length_h,
                      node.tail_map_id,
                      node.tail_left, node.tail_top,
                      node.tail_width, node.tail_height)

        # キャラクター
        pyxel.bltm(self.map_tree[self.current_map_node_id].x * tail_length_w,
                   self.map_tree[self.current_map_node_id].y * tail_length_h,
                   0,
                   self.human.get_tile_x, self.human.get_tile_y,
                   16, 16, 0)

        # テキストボックス
        if self.text_box_flag:
            self.message.text = self.map_tree[self.current_map_node_id].name + "\nhogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehogehoge"
            self.message.show_text_box()

        # カメラ移動
        pyxel.camera(max(0, self.map_tree[self.current_map_node_id].x * tail_length_w - Op.window_w/2), 0)

    def next_scene(self):
        """次のシーンを返すメソッド."""
        return None


if __name__ == "__main__":
    pyxel.init(240, 180)  # (W, H)
    map_scene = MapScene()
    map_scene.update_flame()

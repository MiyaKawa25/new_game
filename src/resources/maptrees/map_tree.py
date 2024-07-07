class MapTree:
    def __init__(self, nodes):
        self.nodes = nodes

    def __getitem__(self, id):
        nodes = [node for node in self.nodes if node.id == id]
        return nodes[0] if len(nodes) > 0 else id

    def get_nearest_upper_sibling_node_id(self, id):
        """最も近い上側の兄弟要素を取得する."""
        # 兄弟要素を抽出
        sibling_nodes = self.__filter_siblings(self.nodes, id)
        # よりyが小さい(上方向にある)要素を抽出
        upper_sibling_nodes = [node for node in sibling_nodes if node.y <= self.nodes[id].y]
        if len(upper_sibling_nodes) < 1:
            return id
        # yが最も近い要素のIDを取得
        nearest_upper_sibling_node = self.__find_node_nearest_y(upper_sibling_nodes, id)
        return nearest_upper_sibling_node.id

    def get_nearest_lowwer_sibling_node_id(self, id):
        """最も近い下側の兄弟要素を取得する."""
        # 兄弟要素を抽出
        sibling_nodes = self.__filter_siblings(self.nodes, id)
        # よりyが大きい(下方向にある)要素を抽出
        lowwer_sibling_nodes = [node for node in sibling_nodes if node.y >= self.nodes[id].y]
        if len(lowwer_sibling_nodes) < 1:
            return id
        # yが最も近い要素のIDを取得
        nearest_lowwer_sibling_node = self.__find_node_nearest_y(lowwer_sibling_nodes, id)
        return nearest_lowwer_sibling_node.id

    def get_nearest_child_node_id(self, id):
        """最も近い子要素を取得する."""
        child_nodes = self.__filter_children(self.nodes, id)
        if len(child_nodes) < 1:
            return id
        nearest_child_node = self.__find_node_nearest_y(child_nodes, id)
        return nearest_child_node.id

    def get_nearest_parent_node_id(self, id):
        """最も近い親要素を取得する."""
        parent_nodes = self.__filter_parents(self.nodes, id)
        if len(parent_nodes) < 1:
            return id
        nearest_parent_node = self.__find_node_nearest_y(parent_nodes, id)
        return nearest_parent_node.id

    def __filter_parents(self, nodes, id):
        """指定されたIDの親要素を抽出する."""
        parent_nodes = [node for node in nodes if id in node.children_ids]
        return parent_nodes

    def __filter_children(self, nodes, id):
        """指定されたIDの子要素を抽出する."""
        child_nodes = [self.nodes[child_id] for child_id in nodes[id].children_ids]
        return child_nodes

    def __filter_siblings(self, nodes, id):
        """指定されたIDの要素と同じ親を持つ要素を抽出する."""
        parent_nodes = self.__filter_parents(nodes, id)
        sibling_nodes = [sibling_node for parent_node in parent_nodes for sibling_node in self.__filter_children(self.nodes, parent_node.id) if sibling_node.id != id]
        return sibling_nodes

    def __find_node_nearest_y(self, nodes, id):
        """指定された要素と最もyが近い要素を1つ返す."""
        # 指定されたyとの差で受け取った要素をソート
        sorted_nodes_by_y_diff = sorted(nodes, key=lambda node: abs(self.nodes[id].y - node.y))
        if len(sorted_nodes_by_y_diff) < 1:
            return self.nodes[id]
        nearest_node = sorted_nodes_by_y_diff[0]
        return nearest_node

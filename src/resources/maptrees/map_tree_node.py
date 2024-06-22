class MapTreeNode:
    def __init__(self, id, name, x, y, children_ids):
        self.id = id
        self.name = name
        self.x = x
        self.y = y
        self.children_ids = children_ids
        # TODO: 以下、タイルマップと要調整
        self.tail_map_id = 0
        self.tail_left = 0
        self.tail_top = 0
        self.tail_width = 8
        self.tail_height = 8
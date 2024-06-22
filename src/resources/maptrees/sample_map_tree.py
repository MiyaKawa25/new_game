from resources.maptrees.map_tree import MapTree
from resources.maptrees.map_tree_node import MapTreeNode

sample_map_tree = MapTree([
    MapTreeNode(0, "1-1", 5, 12, [1]),
    MapTreeNode(1, "1-2", 10, 12, [2,3]),
    MapTreeNode(2, "A1-3", 15, 7, [4]),
    MapTreeNode(3, "B1-3", 15, 17, [4]),
    MapTreeNode(4, "1-4", 20, 12, [5,6,7]),
    MapTreeNode(5, "A1-5", 25, 7, []),
    MapTreeNode(6, "B1-5", 25, 12, [8]),
    MapTreeNode(7, "C1-5", 30, 17, []),
    MapTreeNode(8, "B1-6", 30, 12, [9, 10]),
    MapTreeNode(9, "BA1-7", 35, 6, [11]),
    MapTreeNode(10, "BB1-7", 35, 12, [12]),
    MapTreeNode(11, "BA1-8", 40, 12, [13]),
    MapTreeNode(12, "BB1-8", 37, 18, [14]),
    MapTreeNode(13, "B1-9", 45, 12, [15]),
    MapTreeNode(14, "B1-9", 43, 18, [15]),
    MapTreeNode(15, "B1-9", 50, 17, []),
])
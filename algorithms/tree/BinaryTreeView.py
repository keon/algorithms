import matplotlib.pyplot as plt
import networkx as nx

# Helper class for binary tree node
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Function to build a binary tree from an input array
def build_tree_from_array(arr):
    if not arr:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in arr]
    for i in range(len(nodes)):
        if nodes[i] is not None:
            left_index = 2 * i + 1
            right_index = 2 * i + 2
            if left_index < len(nodes):
                nodes[i].left = nodes[left_index]
            if right_index < len(nodes):
                nodes[i].right = nodes[right_index]

    return nodes[0]

# Function to add edges to the graph for visualization
def add_edges(graph, node, pos, x=0, y=0, level_width=1):
    if node:
        pos[node.value] = (x, y)
        if node.left:
            graph.add_edge(node.value, node.left.value)
            add_edges(graph, node.left, pos, x - level_width, y - 1, level_width / 2)
        if node.right:
            graph.add_edge(node.value, node.right.value)
            add_edges(graph, node.right, pos, x + level_width, y - 1, level_width / 2)

# Function to visualize the tree
def visualize_tree(root):
    if not root:
        print("Tree is empty")
        return

    graph = nx.DiGraph()
    pos = {}
    add_edges(graph, root, pos)

    plt.figure(figsize=(12, 8))
    nx.draw(graph, pos, with_labels=True, arrows=False, node_size=2000,
            node_color='lightblue', font_size=10, font_weight='bold')
    plt.show()

# Example input array representing a binary tree
input_array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
root = build_tree_from_array(input_array)

visualize_tree(root)

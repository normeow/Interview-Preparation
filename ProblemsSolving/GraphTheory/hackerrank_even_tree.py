'''
https://www.hackerrank.com/challenges/even-tree/problem

You are given a tree (a simple connected graph with no cycles). The tree has  nodes numbered from  to  and is rooted at node .

Find the maximum number of edges you can remove from the tree to get a forest
such that each connected component of the forest contains an even number of nodes.
'''


class Node:
    def __init__(self):
        self.children = []
        self.val = 0

    def count_nodes(self):
        if len(self.children) == 0:
            return 1
        res = 1
        for child in self.children:
            res += child.count_nodes()
        return res


def add_children(node, nodes_array, j):
    for i in nodes_array[j]:
        child = Node()
        child.val = i
        node.children.append(child)
        add_children(child, nodes_array, i-1)


def decompose_tree(root):
    res = 0
    nodes = root.children
    while len(nodes) != 0:
        for node in nodes:
            if node.count_nodes() % 2 == 0:
                res += 1
        nodes = [x for node in nodes for x in node.children]
    return res


def solution():
    nodes, edges_num = [int(x) for x in input().split()]
    nodes_array = [[] for _ in range(nodes)]
    for _ in range(edges_num):
        node1, node2 = [int(x) for x in input().split()]
        nodes_array[min(node1, node2)-1].append(max(node1, node2))

    root = Node()
    root.val = 1

    add_children(root, nodes_array, 0)
    print(decompose_tree(root))


solution()

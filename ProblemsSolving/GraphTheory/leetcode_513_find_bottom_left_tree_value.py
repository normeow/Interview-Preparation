# https://leetcode.com/problems/find-bottom-left-tree-value

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        # BFS
        while queue:
            cur_node = queue.pop(0)
            if cur_node.right:
                queue.append(cur_node.right)
            if cur_node.left:
                queue.append(cur_node.left)
        return cur_node.val


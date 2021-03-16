# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.find_depth(root, 0)
    def find_depth(self, root, depth):
        if root is None:
            return depth
        return max(self.find_depth(root.right, depth + 1),self.find_depth(root.left, depth + 1))
            
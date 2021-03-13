# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(root , value):
            if not root:
                return True
            if root.val != value:
                return False
            return check(root.left, value) and check(root.right, value)
        return check(root, root.val)
        
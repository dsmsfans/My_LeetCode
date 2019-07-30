# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0
        temp = 0
        if L <= root.val <= R:
            temp += root.val + self.rangeSumBST(root.right,L,R) + self.rangeSumBST(root.left,L,R)
        elif root.val < L:
            temp += self.rangeSumBST(root.right,L,R)
        elif root.val > R:
            temp += self.rangeSumBST(root.left,L,R)
        return temp
            
            
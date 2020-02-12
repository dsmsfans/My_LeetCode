class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None
        elif root.val == val:
            return root
        elif root.val < val:
            return self.searchBST(root.right,val)
        else:
            return self.searchBST(root.left,val)
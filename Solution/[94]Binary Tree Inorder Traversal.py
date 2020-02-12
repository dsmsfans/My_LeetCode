class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        traversal = []
        def inorder(root):
            if root == None:
                return None
            if root.left != None:
                inorder(root.left)
            traversal.append(root.val)
            if root.right != None:
                inorder(root.right)
        inorder(root)
        return traversal
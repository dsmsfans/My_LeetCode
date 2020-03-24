/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* cal(TreeNode* root, TreeNode* pre)
    {
        if(!root)
        {
            return pre;
        }
        TreeNode* ans = cal(root->left,root);
        root->left = nullptr;
        root->right = cal(root->right, pre);
        return ans;
    }
    TreeNode* increasingBST(TreeNode* root) {
        
        return cal(root,nullptr);
        
    }
};
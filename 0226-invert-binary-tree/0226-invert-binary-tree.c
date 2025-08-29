/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* invertTree(struct TreeNode* root) {
    if (root == NULL){
        return 0;
    }
    else{
        struct TreeNode* tempRoot = root->left;
        root->left = root->right;
        root->right = tempRoot;
    }
    invertTree(root->left);
    invertTree(root->right);

    return root;
}
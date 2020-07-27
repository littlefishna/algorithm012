# Given preorder and inorder traversal of a tree, construct the binary tree. 
# 
#  Note: 
# You may assume that duplicates do not exist in the tree. 
# 
#  For example, given 
# 
#  
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7] 
# 
#  Return the following binary tree: 
# 
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7 
#  Related Topics Array Tree Depth-first Search 
#  👍 3457 👎 93


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind + 1:])
            return root

# leetcode submit region end(Prohibit modification and deletion)

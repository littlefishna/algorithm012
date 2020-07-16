# Given a binary tree, return the inorder traversal of its nodes' values. 
# 
#  Example: 
# 
#  
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# 
# Output: [1,3,2] 
# 
#  Follow up: Recursive solution is trivial, could you do it iteratively? 
#  Related Topics Hash Table Stack Tree 
#  👍 3148 👎 132


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inorderT(node, results):

            if node.left:
                inorderT(node.left, results)

            results.append(node.val)

            if node.right:
                inorderT(node.right, results)

        results = []

        if root is None:
            return []
        inorderT(root, results)
        return results
        
# leetcode submit region end(Prohibit modification and deletion)

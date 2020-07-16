# Given a binary tree, return the preorder traversal of its nodes' values. 
# 
#  Example: 
# 
#  
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# 
# Output: [1,2,3]
#  
# 
#  Follow up: Recursive solution is trivial, could you do it iteratively? 
#  Related Topics Stack Tree 
#  👍 1518 👎 57


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorderT(node, results):
            results.append(node.val)
            if node.left:
                preorderT(node.left, results)
            if node.right:
                preorderT(node.right, results)

        results = []
        if root is None:
            return []
        preorderT(root, results)
        return results
        
# leetcode submit region end(Prohibit modification and deletion)

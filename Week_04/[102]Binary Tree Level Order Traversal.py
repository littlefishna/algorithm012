# Given a binary tree, return the level order traversal of its nodes' values. (i
# e, from left to right, level by level). 
# 
#  
# For example: 
# Given binary tree [3,9,20,null,null,15,7], 
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7
#  
#  
#  
# return its level order traversal as: 
#  
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
#  
#  Related Topics Tree Breadth-first Search 
#  👍 3140 👎 77


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue = [root, '$']
        res = []
        temp_list = []
        while queue:
            t = queue.pop(0)
            if t == '$':
                if len(queue) != 0:
                    queue.append('$')
                res.append(temp_list)
                temp_list = []
                continue
            else:
                temp_list.append(t.val)
            if t.left:
                queue.append(t.left)
            if t.right:
                queue.append(t.right)
        return res
        
# leetcode submit region end(Prohibit modification and deletion)

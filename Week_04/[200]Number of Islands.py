# Given a 2d grid map of '1's (land) and '0's (water), count the number of islan
# ds. An island is surrounded by water and is formed by connecting adjacent lands 
# horizontally or vertically. You may assume all four edges of the grid are all su
# rrounded by water. 
# 
#  
#  Example 1: 
# 
#  
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
#  
# 
#  Example 2: 
# 
#  
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#  
#  Related Topics Depth-first Search Breadth-first Search Union Find 
#  👍 5841 👎 201


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numIslands(self, grid):
        def dfsMarking(i, j, grid):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfsMarking(i - 1, j, grid)
            dfsMarking(i, j - 1, grid)
            dfsMarking(i, j + 1, grid)
            dfsMarking(i + 1, j, grid)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfsMarking(i, j, grid)
                    count += 1
        return count

# leetcode submit region end(Prohibit modification and deletion)
a = Solution()
print(a.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
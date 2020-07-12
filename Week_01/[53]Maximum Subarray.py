# Given an integer array nums, find the contiguous subarray (containing at least
#  one number) which has the largest sum and return its sum. 
# 
#  Example: 
# 
#  
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#  
# 
#  Follow up: 
# 
#  If you have figured out the O(n) solution, try coding another solution using 
# the divide and conquer approach, which is more subtle. 
#  Related Topics Array Divide and Conquer Dynamic Programming 
#  👍 7963 👎 374


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = [nums[0]]
        maxt = nums[0]
        for i in range(1, len(nums)):
            curr.append(max(nums[i]+curr[i-1], nums[i]))
            maxt = max(maxt, curr[i])
        return maxt
        
# leetcode submit region end(Prohibit modification and deletion)

# Given an array of integers, return indices of the two numbers such that they a
# dd up to a specific target. 
# 
#  You may assume that each input would have exactly one solution, and you may n
# ot use the same element twice. 
# 
#  Example: 
# 
#  
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#  
#  Related Topics Array Hash Table 
#  👍 15622 👎 563


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        walked = {}
        for i in range(len(nums)):
            if (target - nums[i]) in walked:
                return [walked[target - nums[i]], i]
            else:
                walked[nums[i]] = i
        return []
# leetcode submit region end(Prohibit modification and deletion)

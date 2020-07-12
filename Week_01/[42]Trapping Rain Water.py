# Given n non-negative integers representing an elevation map where the width of
#  each bar is 1, compute how much water it is able to trap after raining. 
# 
#  
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In 
# this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos
#  for contributing this image! 
# 
#  Example: 
# 
#  
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6 
#  Related Topics Array Two Pointers Stack 
#  👍 7114 👎 122

from __future__ import annotations
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trap(self, height: List[int]) -> int:
        maxfromleft, maxfromright = [0]*len(height), [0]*len(height)
        maxleft, maxright = 0, 0
        water = []
        for i in range(len(height)):
            maxleft = max(height[i], maxleft)
            maxfromleft[i] = maxleft
        for i in range(len(height)-1, -1, -1):
            maxright = max(height[i], maxright)
            maxfromright[i] = maxright
        for i in range(len(height)):
            water.append(
                min(maxfromleft[i], maxfromright[i]) - height[i]
            )
        return sum(water)

a = Solution()
# print(a.findMedianSortedArrays(nums1=[2,2,2,2], nums2=[2,2,2]))
print(a.trap([0,1,0,2,1,0,1,3,2,1,2,1]))

# leetcode submit region end(Prohibit modification and deletion)

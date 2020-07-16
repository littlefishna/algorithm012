# Given an array of strings, group anagrams together. 
# 
#  Example: 
# 
#  
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ] 
# 
#  Note: 
# 
#  
#  All inputs will be in lowercase. 
#  The order of your output does not matter.
#  
#  Related Topics Hash Table String 
#  👍 3564 👎 185


from __future__ import annotations
# leetcode submit region begin(Prohibit modification and deletion)
import collections
class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

a = Solution()
# print(a.findMedianSortedArrays(nums1=[2,2,2,2], nums2=[2,2,2]))
print(a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# leetcode submit region end(Prohibit modification and deletion)

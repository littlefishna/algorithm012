# Given two words (beginWord and endWord), and a dictionary's word list, find al
# l shortest transformation sequence(s) from beginWord to endWord, such that: 
# 
#  
#  Only one letter can be changed at a time 
#  Each transformed word must exist in the word list. Note that beginWord is not
#  a transformed word. 
#  
# 
#  Note: 
# 
#  
#  Return an empty list if there is no such transformation sequence. 
#  All words have the same length. 
#  All words contain only lowercase alphabetic characters. 
#  You may assume no duplicates in the word list. 
#  You may assume beginWord and endWord are non-empty and are not the same. 
#  
# 
#  Example 1: 
# 
#  
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# Output:
# [
#   ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]
# ]
#  
# 
#  Example 2: 
# 
#  
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# Output: []
# 
# Explanation: The endWord "cog" is not in wordList, therefore no possible trans
# formation.
#  
# 
#  
#  
#  Related Topics Array String Backtracking Breadth-first Search 
#  👍 1809 👎 249


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        possibles = [chr(x) for x in range(ord('a'), ord('z') + 1)]
        queue = [(beginWord, 0)]
        queue_steady = {0:[beginWord]}
        seen = set([beginWord])
        if len(beginWord) == 1 and endWord in wordList:
            return [[beginWord, endWord]]


        while queue:
            s, level = queue.pop(0)
            if s == endWord:

                maxl = 0
                len_queue = len(queue_steady)-1
                if len(queue_steady[len_queue]) > 1:
                    queue_steady[len_queue] = [endWord]

                for v in queue_steady.values():
                    maxl = max(maxl, len(v))


                res = [[] for i in range(maxl)]
                for k, v in queue_steady.items():
                    if len(v)<maxl:
                        for i in range(maxl):
                            res[i].append(v[0])
                    else:
                        for i in range(maxl):
                            res[i].append(v[i])

                return res

            for i in range(len(beginWord)):
                for letter in possibles:
                    temp = s[:i] + letter + s[i + 1:]
                    if temp in wordList and temp not in seen:
                        queue.append((temp, level + 1))
                        if level+1 not in queue_steady:
                            queue_steady[level+1] = [temp]
                        else:
                            queue_steady[level+1].append(temp)
                        seen.add(temp)

        return []
        
# leetcode submit region end(Prohibit modification and deletion)
a = Solution()
print(a.findLadders("hot",
"dog",
["hot","cog","dog","tot","hog","hop","pot","dot"]))
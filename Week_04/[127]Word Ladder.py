# Given two words (beginWord and endWord), and a dictionary's word list, find th
# e length of shortest transformation sequence from beginWord to endWord, such tha
# t: 
# 
#  
#  Only one letter can be changed at a time. 
#  Each transformed word must exist in the word list. 
#  
# 
#  Note: 
# 
#  
#  Return 0 if there is no such transformation sequence. 
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
# Output: 5
# 
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog
# " -> "cog",
# return its length 5.
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
# Output: 0
# 
# Explanation: The endWord "cog" is not in wordList, therefore no possible trans
# formation.
#  
# 
#  
#  
#  Related Topics Breadth-first Search 
#  👍 3259 👎 1181


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        possibles = [chr(x) for x in range(ord('a'), ord('z') + 1)]
        queue = [(beginWord, 0)]
        seen = set()
        while queue:
            s, level = queue.pop(0)
            if s == endWord:
                return level + 1

            for i in range(len(beginWord)):
                for letter in possibles:
                    temp = s[:i] + letter + s[i + 1:]
                    if temp in wordList and temp not in seen:
                        wordList.remove(temp)
                        queue.append((temp, level + 1))
                        seen.add(temp)

        return 0
a = Solution()
a.ladderLength(beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"])
        
# leetcode submit region end(Prohibit modification and deletion)

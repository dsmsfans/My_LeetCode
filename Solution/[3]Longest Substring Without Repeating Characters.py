class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        dic = []
        for i in s:
            if i in dic:
                length = max(len(dic),length)
                del dic[0:dic.index(i) + 1]
            dic.append(i)
            length = max(len(dic),length)
        return length


                
                
                    
                    
            
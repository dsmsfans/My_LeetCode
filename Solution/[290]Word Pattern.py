class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        map1 = {}
        map2 = {}
        words = s.split(' ')
        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in map1:
                map1[pattern[i]] = words[i]
            elif map1[pattern[i]] != words[i]:
                return False
            else:
                pass
        for j in range(len(words)):
            if words[j] not in map2:
                map2[words[j]] = pattern[j]
            elif map2[words[j]] != pattern[j]:
                return False
            else:
                pass
        return True
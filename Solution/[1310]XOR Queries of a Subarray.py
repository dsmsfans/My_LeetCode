class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        prefix = [0] + arr
        for i in range(len(arr)):  # you can modify the arr directly 
            prefix[i+1]^=prefix[i]
        ans = []
        for left,right in queries:
            ans.append(prefix[right+1]^prefix[left])

        return ans
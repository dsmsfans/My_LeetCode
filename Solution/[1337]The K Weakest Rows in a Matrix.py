class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        dict1={}
        count = 0
        for row in mat:
            dict1[count] = sum(row)
            count += 1
        output = sorted(dict1.items(), key=lambda x:x[1])
        return [x for x, y in output[0:k]]
            
        
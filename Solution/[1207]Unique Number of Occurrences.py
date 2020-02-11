class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 1:
            return False
        number = set(arr)
        num_count = []
        for num in number:
            num_count.append(arr.count(num))
            
        if len(number) == len(set(num_count)):
            return True
        else:
            return False
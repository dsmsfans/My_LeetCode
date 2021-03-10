class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        output = 0
        for i in range(len(arr) - 2):
            x = arr[i]
            for j in range(i + 1, len(arr) - 1):
                y = arr[j]
                if(abs(x - y) <= a):
                    for k in range(j + 1, len(arr)):
                        z = arr[k]
                        if(abs(y - z) <= b and abs(x - z) <= c):
                            output = output + 1
        return output
                        
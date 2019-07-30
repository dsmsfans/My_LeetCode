class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        B_x = list(bin(x)[2::])
        B_y = list(bin(y)[2::])
        fill = abs(len(B_x) - len(B_y))
        zero = ['0'] * fill
        if len(B_x) > len(B_y):
            B_y = zero + (B_y)
        else:
            B_x = zero + (B_x)
        num = 0
        for i in range(len(B_x)):
            if B_x[i] != B_y[i]:
                num += 1
        return num
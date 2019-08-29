class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices:
            earn = 0
            for i in range(1,len(prices)):
                if prices[i] > prices[i - 1]:
                    earn = earn + prices[i] - prices[i - 1]
            return earn
        else:
            return 0
        
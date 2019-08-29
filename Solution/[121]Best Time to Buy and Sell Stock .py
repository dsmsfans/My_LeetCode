class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices:
            earn = 0
            total = 0
            for i in range(1,len(prices)):
                earn = max(0,earn + prices[i] - prices[i - 1])
                total = max(earn,total)
            return total
        else:
            return 0 
        
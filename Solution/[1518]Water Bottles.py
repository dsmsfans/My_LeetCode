class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        empty = numBottles
        exchange = 0
        output = numBottles
        while empty >= numExchange:
            exchange = int(empty / numExchange)
            empty = exchange + (empty % numExchange)
            output += exchange
        return output
        
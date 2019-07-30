class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0
        left = 0
        result = 0
        right = len(height) - 1
        while right > left:
            width = right - left
            result = max(result,min(height[right],height[left]) * width)
            print(min(height[right],height[left]) * width)
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return result
        
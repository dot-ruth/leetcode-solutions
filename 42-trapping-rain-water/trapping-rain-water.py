class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        l, r = 0, len(height)-1
        left_max = height[l]
        right_max = height[r]
        while l < r:
            if left_max < right_max:
                l += 1 
                left_max = max(height[l], left_max)
                res += left_max - height[l]
            else:
                r -= 1
                right_max = max(height[r], right_max)
                res += right_max - height[r]
        return res

        
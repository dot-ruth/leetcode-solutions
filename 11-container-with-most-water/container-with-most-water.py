class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # time complexity = O(n^2) -- brute force solution 
        # res = 0 
        # for l in range(len(height)):
        #     for r in range(l+1, len(height)):
        #         area = (r - l) * min(height[l],height[r])
        #         res = max(res, area)
        # return res 

        # time compelxity = O(n)
        res = 0 
        l,r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[l],height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -=1
        return res
        
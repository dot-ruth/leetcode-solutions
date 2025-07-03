class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # time limit exceeded (brute-force approach)
        # r = 0
        # res = []
        # for l in range(len(nums)):
        #     r = l + k 
        #     if r <= len(nums):
        #         res.append(max(nums[l:r]))
        # return res 
        res = []
        l = r = 0
        q = collections.deque()

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if l > q[0]:
                q.popleft()
            if ( r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res

        
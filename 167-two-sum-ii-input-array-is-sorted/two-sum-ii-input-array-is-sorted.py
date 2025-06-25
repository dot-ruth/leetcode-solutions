class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsDict = {}
        for i,num in enumerate(numbers):
            value_num = target - num
            if value_num in numsDict:
                return [numsDict[value_num], i+1]
            numsDict[num] = i+1
        return []
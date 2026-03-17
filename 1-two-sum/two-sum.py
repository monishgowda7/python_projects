class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a={}
        for i in range(len(nums)):
            complement=target-nums[i]

            if complement in a:
                return a[complement],i

            a[nums[i]]=i
        
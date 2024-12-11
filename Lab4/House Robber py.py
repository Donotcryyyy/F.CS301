class Solution(object):
    def rob(self, nums):
        
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        prev2, prev1 = 0, 0  

        for num in nums:
            curr = max(prev1, prev2 + num)  
            prev2, prev1 = prev1, curr  

        return prev1

class Solution:
    def sortedArrayToBST(self, nums):
        return self.sortedArrayToBSTHelper(nums, 0, len(nums) - 1)


    def sortedArrayToBSTHelper(self, nums, left, right):
        if left > right:
            return None

        mid = (left + right) // 2  
        root = TreeNode(nums[mid]) 

      
        root.left = self.sortedArrayToBSTHelper(nums, left, mid - 1)
        root.right = self.sortedArrayToBSTHelper(nums, mid + 1, right)

        return root


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

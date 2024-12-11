class Solution:
    def sortArray(self, nums):
        if not nums or len(nums) <= 1:
            return nums
        return self.mergeSort(nums)

    
    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums

    
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

 
        left = self.mergeSort(left)
        right = self.mergeSort(right)

      
        return self.merge(left, right)


    def merge(self, left, right):
        result = []
        i = j = 0

       
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

       
        result.extend(left[i:])
        result.extend(right[j:])

        return result

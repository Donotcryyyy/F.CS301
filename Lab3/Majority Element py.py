class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        # Boyer-Moore Voting Algorithm
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate

# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums1 = [3, 2, 3]
    nums2 = [2, 2, 1, 1, 1, 2, 2]

    print("Majority Element in nums1:", solution.majorityElement(nums1))  # Output: 3
    print("Majority Element in nums2:", solution.majorityElement(nums2))  # Output: 2

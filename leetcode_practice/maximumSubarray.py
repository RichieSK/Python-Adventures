# Problem: Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# Time Complexity : O(n)
# Space Complexity: O(1)

# General Idea: Let's consider the array that would satisfy the given condition and look at a certain property.
# As we add each element of that resultant array to the array, the sum cannot drop below 0. Otherwise, we can ignore that part of the array
# and take the sum of the remaining elements.
# By using the above, let's consider two things as we iterate through the array and take the sum of the sub-array from the leftmost position.
# 1. If the sum of the elements of the sub array add up to a positive number, add the new number to it. If this new sum is greater than our max sum,
# then update our max sum.
# 2. If the sum of the elements of the sub array add up to a negative number, discard the array and start the new sub array from the new element.
class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         left = 0
#         right = 1
#         maxSum = nums[0]
#         currentSum = nums[0]
#         while right < len(nums):
#             if currentSum < 0:
#                 left = right
#                 currentSum = 0
#             currentSum += nums[right]
#             if currentSum > maxSum:
#                 maxSum = currentSum
#             right += 1
#         return maxSum
    def maxSubArray(self, nums: List[int]) -> int:
        maxNum = nums[0]
        for i in range(1,len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            if nums[i] > maxNum:
                maxNum = nums[i]
        return maxNum

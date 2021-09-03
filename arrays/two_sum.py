"""
Problem:

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.
"""
from typing import List


# Time: O(n^2), Space: O(1)
class Solution:
    """
    This solution iterates through the array in a nested fashion, exhaustively
    checking every combination of two numbers in the array. If the sum of those
    two numbers equal the target number, we can return the indices of those two
    numbers, since we know there is exactly one solution in the input array.
    This nested looping implies a time complexity of O(n^2).
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Time: O(n), Space: O(n)
class Solution:
    """
    Rather than check if the sum of two values in the array are equal to the
    target number, we can calculate the (target - nums[i]) at each index i in the
    array. Then we check if the resulting difference appeared previously in the
    array. Given that there is exactly one solution in the input, we know if
    (target - nums[i]) exists exactly once elsewhere in the array. 
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in d:
                return [d[diff], i]
            d[nums[i]] = i
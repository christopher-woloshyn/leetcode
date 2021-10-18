"""
Problem:

Given an integer array nums, return an array answer such that answer[i] is equal
to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
integer.

You must write an algorithm that runs in O(n) time and without using the
division operation.
"""
from typing import List

# Time: O(n), Space: O(n), includes division.
class Solution:
    """
    First we take the poduct of every number in the array. Then, for each value
    in the array we divide the product by that value and append it to that index
    of the resulting array.
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        for n in nums:
            product *= n

        return [product // num for num in nums]

# Time O(n^2), Space O(n)
class Solution:
    """
    To complete this problem without the division operator, we need to compute
    the product of all items in the array BEFORE and AFTER each item in the
    array, not including itself. This can be done in a brute force fashion by
    multiplying through all numbers of the array excluding the current value.
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
            
            ans.append(product)
        
        return ans

# Time O(n), Space O(n)
class Solution:
    """
    To complete this problem without the division operator, we can compute a
    "prefix" and "postfix" value that stores the product of all preceding or
    succeeding values respectively. A value's product-except-self will be the
    prefix value multiplied with the postfix value for that value's index.
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        pre = 1
        post = 1

        for i in range(len(nums)):
            ans[i] *= pre
            ans[-(i+1)] *= post
            pre *= nums[i]
            post *=nums[-(i+1)]
        
        return ans

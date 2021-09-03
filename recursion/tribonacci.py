"""
Problem:

The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""
class Solution:
    """
    Calculates the Nth Tribonacci number using a recursive approach.
    This is similar to how a Fibonacci number is calculated.
    """
    def tribonacci(self, n: int) -> int:
        if n >= 3:
            return (
                self.tribonacci(n-3) +
                self.tribonacci(n-2) +
                self.tribonacci(n-1)
            )
        elif n > 0:
            return 1
        else:
            return 0
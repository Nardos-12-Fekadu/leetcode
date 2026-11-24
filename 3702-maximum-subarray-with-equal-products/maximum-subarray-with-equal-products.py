
from math import gcd, lcm
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        longest = 0

        for i in range(len(nums)):
            product = 1
            g = 0
            L = 1

            for j in range(i, len(nums)):
                product *= nums[j]
                g = gcd(g, nums[j])
                L = lcm(L, nums[j])

                if product == g * L:
                    longest = max(longest, j - i + 1)

        return longest

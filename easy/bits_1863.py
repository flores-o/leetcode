"""
1863. Sum of All Subset XOR Totals

The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
Given an array nums, return the sum of all XOR totals for every subset of nums. 

Note: Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.

Example 1:

Input: nums = [1,3]
Output: 6
Explanation: The 4 subsets of [1,3] are:
- The empty subset has an XOR total of 0.
- [1] has an XOR total of 1.
- [3] has an XOR total of 3.
- [1,3] has an XOR total of 1 XOR 3 = 2.
0 + 1 + 3 + 2 = 6
"""
from functools import reduce
from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xorred_subsets = self.subsets(nums)
        return reduce(lambda x, y: x + y, xorred_subsets)


    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [0]
        
        subs = self.subsets(nums[1:])
        res = subs[:]

        for elem in subs:
            res.append(nums[0] ^ elem)
        return res
    
class Solution2:
    def subsetXORSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        result = 0
        for subset_respresentation in range(1<<n):
            xorred_subset = 0
            for j in range(n):
                if subset_respresentation & (1 << j):
                    xorred_subset ^= nums[j]
            result += xorred_subset
        return result
        
        




if __name__ == "__main__":
    sol = Solution()
    assert(sol.subsetXORSum([1,3]) == 6)
    assert(sol.subsetXORSum([5,1,6]) == 28)

    sol2 = Solution2()
    assert(sol2.subsetXORSum([1,3]) == 6)
    assert(sol2.subsetXORSum([5,1,6]) == 28)
"""
You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.

Input: nums = [3,2,3,2,2,2]
Output: true
Explanation: 
There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.
"""
from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) % 2 != 0:
            return False
        nums.sort()
        for i in range(0, len(nums), 2):
            if nums[i] != nums[i+1]:
                return False
        return True
    
    def countSetBits(self, n):
        count = 0
        while (n):
            count += n & 1
            n >>= 1
        return count
    
    def toggleBit(self, bitmask, bit):
        return bitmask ^ (1 << bit)
    
    def divideArrayBitManipulation(self, nums: List[int]) -> bool:
        if len(nums) % 2 != 0:
            return False
        
        bitmask = 2<<501
        for num in nums:
            bitmask = self.toggleBit(bitmask, num)
        
        return self.countSetBits(bitmask) == 1

if __name__ == "__main__":
    sol = Solution()
    assert(sol.divideArrayBitManipulation([3,2,3,2,2,2]) == True)
    assert(sol.divideArrayBitManipulation([3,2,3,2,2,2,2]) == False)        


        

"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
"""
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        return [self.countBitsHelper2(i) for i in range(n+1)]
    
    def countBitsHelper(self, a: int) -> List[int]:

        counter = 0
        while a:
            if a & 1:
                counter += 1
            a >>= 1
        return counter

    def countBitsHelper2(self, a: int) -> List[int]:
        """
        rewrite the above function as a one-liner
        """
        return sum([1 for i in range(32) if a & (1 << i)])

if __name__ == "__main__":
    sol = Solution()
    assert(sol.countBits(2) == [0,1,1])
    assert(sol.countBits(5) == [0,1,1,2,1,2])
    assert(sol.countBits(0) == [0])

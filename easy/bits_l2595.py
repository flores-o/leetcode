"""
You are given a positive integer n.

Let even denote the number of even indices in the binary representation of n (0-indexed) with value 1.

Let odd denote the number of odd indices in the binary representation of n (0-indexed) with value 1.

Return an integer array answer where answer = [even, odd].

Example 1:

Input: n = 17
Output: [2,0]
Explanation: The binary representation of 17 is 10001. 
It contains 1 on the 0th and 4th indices. 
There are 2 even and 0 odd indices.

Example 2:

Input: n = 2
Output: [0,1]
Explanation: The binary representation of 2 is 10.
It contains 1 on the 1st index. 
There are 0 even and 1 odd indices.
"""
from typing import List

class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even_counter = 0
        odd_counter = 0

        for idx in range(32):
            if n & (1<<idx):
                if idx % 2:
                    odd_counter += 1
                else:
                    even_counter += 1
        return [even_counter, odd_counter]

class Solution2:
    def evenOddBit(self, n: int) -> List[int]:
        even_bits = sum([1 for i in range(32) if i % 2 == 0 and n & (1 << i)])
        odd_bits = sum([1 for i in range(32) if i % 2 == 1 and n & (1 << i)])
        return [even_bits, odd_bits]
        
    
if __name__ == '__main__':
    assert(Solution().evenOddBit(17)==[2,0])
    assert(Solution().evenOddBit(2)==[0,1])
    assert(Solution().evenOddBit(1)==[1,0])
    assert(Solution().evenOddBit(0)==[0,0])

    assert(Solution2().evenOddBit(17)==[2,0])
    assert(Solution2().evenOddBit(2)==[0,1])
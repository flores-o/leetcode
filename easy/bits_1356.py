"""
You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.
Return the array after sorting it.


Example 1:

Input: arr = [0,1,2,3,4,5,6,7,8]
Output: [0,1,2,4,8,3,5,6,7]
Explantion: [0] is the only integer with 0 bits.
[1,2,4,8] all have 1 bit.
[3,5,6] have 2 bits.
[7] has 3 bits.
The sorted array by bits is [0,1,2,4,8,3,5,6,7]
"""
from functools import cmp_to_key
from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))
   
class Solution2:
    def countBits(self, n):
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count
    
    def compareNumbers(self, a, b):
        if self.countBits(a) == self.countBits(b):
            return a - b
        return self.countBits(a) - self.countBits(b)
    
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=cmp_to_key(self.compareNumbers))




if __name__ == '___main___':
    assert(Solution().sortByBits([0,1,2,3,4,5,6,7,8])==[0,1,2,4,8,3,5,6,7])
    assert(Solution().sortByBits([1024,512,256,128,64,32,16,8,4,2,1])==[1,2,4,8,16,32,64,128,256,512,1024])

    assert(Solution2().sortByBits([0,1,2,3,4,5,6,7,8])==[0,1,2,4,8,3,5,6,7])
    assert(Solution2().sortByBits([1024,512,256,128,64,32,16,8,4,2,1])==[1,2,4,8,16,32,64,128,256,512,1024])
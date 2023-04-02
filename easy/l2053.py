"""
2053. Kth Distinct String in an Array

Companies
A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.

 

Example 1:

Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"
Explanation:
The only distinct strings in arr are "d" and "a".
"d" appears 1st, so it is the 1st distinct string.
"a" appears 2nd, so it is the 2nd distinct string.
Since k == 2, "a" is returned. 
Example 2:

Input: arr = ["aaa","aa","a"], k = 1
Output: "aaa"
Explanation:
All strings in arr are distinct, so the 1st string "aaa" is returned.
Example 3:

Input: arr = ["a","b","a"], k = 3
Output: ""
Explanation:
The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".
 

Constraints:

1 <= k <= arr.length <= 1000
1 <= arr[i].length <= 5
arr[i] consists of lowercase English letters.
"""
from typing import List

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = {}
        for idx, elem in enumerate(arr):
            if elem not in freq.keys():
                freq[elem] = {'freq': 0, 'idx': 0}
            freq[elem]['freq'] += 1
            freq[elem]['idx'] = idx
        distinct_elem = [elem for elem in freq.keys() if freq[elem]['freq'] == 1]

        sorted_keyes = sorted(distinct_elem, key=lambda x: freq[x]['idx'])

        if k > len(sorted_keyes):
            return ""
        return sorted_keyes[k-1]
                
    def kthDistinctAlternative(self, arr: List[str], k: int) -> str:
        freq = {}
        for idx, elem in enumerate(arr):
            if elem not in freq.keys():
                freq[elem] = 1
            else:
                freq[elem] = -1
                

        distinct_elem = [elem for elem in arr if freq[elem] == 1]

        if k > len(distinct_elem):
            return ""
        else:
            return distinct_elem[k-1]

if __name__ == '__main__':
    s = Solution()
    arr = ["d","b","c","b","c","a"]
    k = 2
    print(s.kthDistinct(arr, k))


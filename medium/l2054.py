"""
2054. Two Best Non-Overlapping Events
Medium
Companies
You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei]. The ith event starts at startTimei and ends at endTimei, and if you attend this event, you will receive a value of valuei. You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.

Return this maximum sum.

Note that the start time and end time is inclusive: that is, you cannot attend two events where one of them starts and the other ends at the same time. More specifically, if you attend an event with end time t, the next event must start at or after t + 1.

 

Example 1:


Input: events = [[1,3,2],[4,5,2],[2,4,3]]
Output: 4
Explanation: Choose the green events, 0 and 1 for a sum of 2 + 2 = 4.
"""
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        sorted_events = sorted(events, key=lambda x: x[1])

        max_sum = 0
        for idx in range(len(sorted_events)):
            for idx2 in range(idx+1, len(sorted_events)):
                if sorted_events[idx][1] < sorted_events[idx2][0]:
                    max_sum = max(max_sum, sorted_events[idx][2] + sorted_events[idx2][2])
            max_sum = max(max_sum, sorted_events[idx][2])
        return max_sum

'''
1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        
        for i in range(len(nums)):
            key = target - nums[i]
            if key in d:
                return [d[key], i]
            else:
                d[nums[i]] = i
                
        return []
    
'''
nums = [2,7,11,15]
target = 9

+-------+------------+----------+------------------------+----------+---------+
|       |    nums[i] | d before | key = target - nums[i] | key in d | d after |
+-------+------------+----------+------------------------+----------+---------+
| i = 0 |          2 | {}       | 9 - 2 = 7              | false    | {2:0}   |
| i = 1 |          7 | {2:0}    | 9 - 7 = 2              | true     |         |
+-------+------------+----------+------------------------+----------+---------+   
'''

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum(nums=[2,7,11,15],target=9))

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

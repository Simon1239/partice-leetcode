# coding:utf-8

from typing import List

class Solution:
    def removeDuplicattes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        return slow
    
if __name__=='__main__':
    nums = [1,1,2]
    S = Solution()
    print(S.removeDuplicattes(nums))
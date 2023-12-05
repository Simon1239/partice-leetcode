# coding:utf-8

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best = 10**7

        # 根据差值的绝对值来更新答案
        def update(cur):
            nonlocal best
            if abs(cur - target) < abs(best - target):
                best = cur

        # 枚举a
        for i in range(n):
            # 保证和上一次的元素不相等
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 使用双指针枚举b和c
            j, k = i+1, n-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                # 如果和为target直接返回答案
                if s == target:
                    return target
                update(s)
                if s > target:
                    # 如果和大于target，移动c对应的指针
                    k0 = k - 1
                    # 移动到下一个不相等的元素
                    while j < k0 and nums[k0] == nums[k]:
                        k0 -= 1
                    k = k0
                else:
                    # 如果和小于target，移动b对应的指针
                    j0 = j + 1
                    # 移动到下一个不相等的元素
                    while j0 < k and nums[j0] == nums[j]:
                        j0 += 1

                    j = j0
        
        return best

if __name__ == '__main__':
    S = Solution()
    print(S.threeSumClosest([-1,2,1,-4],1))
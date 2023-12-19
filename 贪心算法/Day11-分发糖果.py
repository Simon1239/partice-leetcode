# coding:utf-8 

from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [0]*n
        for i in range(n):
            if i > 0 and ratings[i] > ratings[i-1]: # 左侧规则
                left[i] = left[i-1] + 1
            else:
                left[i] = 1

        right = ret = 0
        for i in range(n-1, -1, -1):
            if i < n-1 and ratings[i] > ratings[i+1]:
                right += 1
            else:
                right = 1

            ret += max(left[i], right)

        return ret
    
if __name__ == '__main__':
    S =Solution()
    ratings = [1,0,2]
    print(S.candy(ratings))
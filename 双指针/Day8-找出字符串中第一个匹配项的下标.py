# coding:utf-8

class Solution:
    def strStr(self, haystask:str, needle:str) -> int:
        #  暴力匹配
        for i in range(0, len(haystask)-len(needle)+1):
            if haystask[i:i+len(needle)] == needle:
                return i
        return -1
    

if __name__ == '__main__':
    haystack = 'sadbutsad'
    needle = 'sad'
    S = Solution()
    print(S.strStr(haystack, needle))
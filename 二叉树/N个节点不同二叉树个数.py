# -*- coding: utf-8 -*-
# Author   : ZhangQing
# Time     : 2023/11/14 15:53
# File     : N个节点不同二叉树个数.py
# Project  : Test
# Desc     : 增加缓存

def count(n):
    # root  : 1
    # left  : k [0, n-1]
    # right : n-1-k

    s = count.cache.get(n, 0)
    if s:
        return s

    for k in range(n):
        s += count(k) * count(n - 1 - k)

    count.cache[n] = s
    return s

count.cache = {0:1}

print(count(100))
print(count.cache)
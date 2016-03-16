#!/usr/bin/env python
# coding:utf8
# By:dub
'''
给定一个列表,元素为int类型
给出一个数（列表里面任意两个元素的和）
求两个元素位置

'''

class Solution(object):
    def twosum(self, nums, target):
        new_nums = sorted(nums)
        left = 0
        right = len(nums) - 1

        while left < right:
            val = new_nums[left] +  new_nums[right]
            if val == target:
                break
            elif val < target:
                left += 1
            elif val > target:
               right -= 1
        if left == right:
            return -1,-1
        else:
            p1 = nums.index(new_nums[left])
            p2 = nums.index(new_nums[right])
            if p1 == p2:
                # 将列表分成两段，求出第二段元素位置。
                p2 = nums[p1+1:].index(new_nums[right])+p1+1


        return min(p1,p2),max(p1,p2)

s = Solution()
print s.twosum([2,3,1,4],7) # excepted (1,3)
s1 = Solution()
print s1.twosum([2,0,3,4,0,5,0],0) #excepted(1,4)


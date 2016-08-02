'''
Created on 2016年8月2日

@author: xianxun
'''

def twosum(nums, target):
    a = 0
    b = 0
    c = 0
    d = 0
    f = 0;
    for i in range(0, len(nums)):
        a = nums[i]
        b = target - a
        c = i
        for j in range(i, len(nums)):
            if nums[j] == b:
                d = j
                f = 1
        if f == 1:
            break         
                
    print(c, d)

twosum([2, 7, 11, 15, 9, 8, 7], 14)

        
        
        

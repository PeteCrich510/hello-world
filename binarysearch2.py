# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 09:43:48 2021

@author: petda
"""

list=[1,2,3,4,5,6,7]
start = 0
end = len(list)
midpoint = (end+start)//2
key = int(input("what element do you want"))
while key != list[midpoint]:
    if key > list[midpoint]:
        list = list[midpoint:]
        start = midpoint
        midpoint = (end+start)//2
    else:
        list = list[:midpoint]
        end = midpoint
        midpoint = (end+start)//2
        
print(f'we have found our value {key} at index {midpoint}')
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 09:14:16 2021

@author: petda
"""
# def binary_search_iterative(list, key):
  # if(key == list[midpoint]):
  #       we found the element
  #   elif(key>list[midpoint]):
  #       list = [midpoint:]
  #       else key<list[midpoint]
  #       list = [:midpoint]

list = [1,2,3,4,5,6,7]
midpoint = len(list)//2
key = int(input("what value 1-7 would you like to find"))
while key != list[midpoint]:
    if key > list[midpoint]:
        list = list[midpoint:]
        midpoint = len(list)//2
    else:
        list = list[:midpoint]
        midpoint = len(list)//2
        
print(f'we have found our index value at {midpoint}')

#this gives a new list every time, check binary search 2 on 10-6-21 classwork
   
    
    


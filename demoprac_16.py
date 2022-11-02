# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 11:54:29 2022

@author: Admin
"""



N = int(input("Enter the number of students:"))
kids = []
for n in range(N):
    kids.append(int(input("Enter the marks of students:")))

def candy(ratings):
    count = 1
    candies = [1]
    for index in range(1, len(ratings)):
        if ratings[index]==0:
            count = 1
            
        elif ratings[index] > ratings[index - 1]:
            count += 1
            print(count)
        else:
            count = 1
            print(count)
        candies.append(count)
        
    return candies

ll = candy(kids)
kids.reverse()
lr = candy(kids)
print(sum(map(max, zip(ll, reversed(lr)))))
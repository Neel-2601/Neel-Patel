# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 12:21:27 2022

@author: Admin
"""

import matplotlib.pyplot as pt
recursion,loop,eq=[],[],[]
n=input("Enter Numbers: ").split()
print("Recursion:")
def rec(n):
 global p
 p=p+1
 if n>1:
     p=p+1
     return n + rec(n-1)
 else:
     p=p+1
 return n

for i in range(len(n)):
 q=int(n[i])
 p=0
 print("Answer :", rec(q))
 print('Count :', p)
 recursion.append(p)

print("Loop:-")
for i in range(len(n)):
 ans = 0
 p=0
 q=int(n[i])
 for i in range(1, q+1, 1):
     ans=ans+i
     p=p+1
 print("Answer :", ans)
 print('Count :',p)
 loop.append(p)

print("Equation:-")
for i in range(len(n)):
 p=0
 q=int(n[i])
 number=q*(q+1)/2
 p=p+1
 print("Answer: ", number)
 print('Count: ',p)
 eq.append(p)
pt.plot(n,recursion,label = "RECURSSION")
pt.plot(n,loop,label = "LOOP")
pt.plot(n,eq,label = "EQUATION")
pt.ylabel("COUNTS")
pt.title("COMPARE")
pt.legend()
pt.show()

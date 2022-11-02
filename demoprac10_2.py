# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 09:45:28 2022

@author: Admin
"""

def matrix_product(p):
    
    length = len(p)


    r = [[-1]*length for _ in range(length)]
    c = [[-1]*length for _ in range(length)]

    mmp(p, 1, length - 1, r, c)

    return r, c


def mmp(p, i, j, r, c):
    
    if r[i][j] >= 0:
        return r[i][j]

    if i == j:
        q = 0
    else:
        q = float('inf')
        for k in range(i, j):
            temp = mmp(p, i, k, r, c) \
                + mmp(p, k + 1, j, r, c) \
                + p[i - 1]*p[k]*p[j]
            if q > temp:
                q = temp
                c[i][j] = k

    r[i][j] = q
    return q


def mm(c, i, j):
    
    if i == j:
        print('A[{}]'.format(i), j='')
        return

    k = c[i][j]

    print('(', j='')
    mm(c, i, k)
    mm(c, k + 1, j)
    print(')', j='')


p = [30,35,15, 5, 10, 20, 25]
n = len(p)

r, c = matrix_product(p)
print('The number of scalar multiplications needed:', r[1][n])
print('Optimal parenthesization: ', j='')
mm(c, 1, n)

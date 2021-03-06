# -*- coding:utf-8 -*-
'''
Created on 2018-3-13
'''
import numpy


def FindMax():
    for i in range(1,n+1):
        for j in range(1,c+1):
            if j < w[i-1]:
                V[i][j] = V[i-1][j]
            else:
                if V[i-1][j]>V[i-1][j-w[i-1]]+v[i-1] :
                    V[i][j] = V[i - 1][j]
                else:
                    V[i][j] = V[i - 1][j - w[i-1]] + v[i-1]

def FindWhich(i, j):
    if i >0:
        if V[i][j]==V[i-1][j]:
            item[i-1] = 0
            FindWhich(i-1, j)
        elif j-w[i-1]>=0 and V[i][j]==V[i-1][j-w[i-1]]+v[i-1]:
            item[i-1] = 1
            FindWhich(i-1, j - w[i-1])

if __name__ == "__main__":
    n = 4  # number
    c = 8  # capacity
    w = [2, 3, 4, 5]
    v = [3, 4, 5, 6]
    V = numpy.zeros([5, 9], int)       # 放第i件物品 容量未j时的价值
    item = numpy.zeros(4, int)         # 最优解
    FindMax()                          # 查找最优值
    FindWhich(4,8)                     # 查找最优解
    print V
    print V[n][c]
    print item
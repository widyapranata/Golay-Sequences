2# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 12:33:46 2021

@author: ASUS
"""

import itertools
list_user = []
list_panjang = int(input("Masukan Panjang list : "))
for i in range(0, list_panjang):
    list_user.append(1)

n = len(list_user)

def kombinasi(a, j):
    for i in range(0, j+1):
        if i > 0:
            a[n-i] = -1
    return a
def permutasi(b):
    Na = set(itertools.permutations(b))
    return Na
def is_coplimentari(list_a,list_b):
    for i in range(0, len(list_a)):
        if i > 0:
            if list_a[i] + list_b[i] != 0:
                return False
    return True

for i in range(0, n+1):
    tmp = kombinasi(list_user, i)
    a = permutasi(tmp)
    for j in a:
        list_a = j
        tmp = kombinasi(list_user, i)
        b = permutasi(tmp)
        for k in b:
            list_b = k
            Na = []
            Nb = [] 
            for l in range(0, n):
                tmpa = []
                tmpb = []
                if l == 0:
                    tmpA = 0
                    tmpB = 0
                    for i in range(0, n):
                        tmpA += list_a[i]**2
                        tmpB += list_b[i]**2
                    Na.append(tmpA)
                    Nb.append(tmpB)
                else:
                    jn = l
                    for m in range(0, n-l):
                        tmpA = 0
                        tmpB = 0
                        tmpA = list_a[m] * list_a[jn]
                        tmpB = list_b[m] * list_b[jn]
                        tmpa.append(tmpA)
                        tmpb.append(tmpB)
                    if m == n-l-1:
                        tmpA = 0
                        tmpB = 0
                        for i in range(0, len(tmpa)):
                            tmpA += tmpa[i]
                            tmpB += tmpb[i]
                        Na.append(tmpA)
                        Nb.append(tmpB)
            complimentary = is_coplimentari(Na,Nb)
            if complimentary:
                print("Barisan Complimentary")
                print("a :",list_a)
                print("b :",list_b)                
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 19:15:52 2019

@author: iangu
"""
import builtwith
import whois

#f(n) = f(n-1)+f(n-2) n>=2
#       1             n >= 0 n为自然数

def Fab(n):
#    递归调用的出口
    if n == 0 or n == 1:
        return 1
#    递归
    return Fab(n-1)+Fab(n-2)

print(Fab(3))



#def minMax(L,start,end):
#    
#    if end - start <= 1:
#        return (max(L[start],L(end)),min(L[start],L(end)))
#    else:
#        max1,min1 = minMax(L[start:(start+end)/2],start,(start+end)/2)
#        max2,min2 = minMax(L[(start+end)/2],(start+end)/2,end)
#        return (max([max1,max2]),min([min1,min2]))
#            
#        
#list1 = [1,5,3,6,4,8,5,10] 
#print(minMax(list1,0,len(list1)))


print(builtwith.parse("http://www.sina.com.cn"))

print(whois.whois("http://www.baidu.com"))
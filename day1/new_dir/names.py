#!/usr/bin/python3
#-*-coding:utf-8 -*-
# Author:dlj

#names=["4zhangyang","guyun","#!xiangpeng","Xchengronghua","zhangyang","xuliangchen"]
import copy
# # print(names)
# # print(names[1:3])#切片
# # print(names[-1])#切片
# # print(names[-2])#切片
# # print(names[-2:])#切片
# # print(names[:3])#切片
# print(names)
# names.append("leihaidong")
# print(names)
# names.insert(1,"chenronghua")有很多的算法需要用指针有很多的算法需要用指针来实现，这其中就包括链表、二叉树、图、最小生成树等等。今天，为了给大家说明如何利用来实现，这其中就包括链表、二叉树、图、最小生成树等等。今天，为了给大家说明如何利用
# print(names)
# names.insert(3,"xinzhiyun")
# print(names)
# names[2]="xiedi"
# print(names)
# #delete
# names.remove("chenronghua")
# print(names)
# del names[1]
# print(names)
# names.pop(1)#输入下标，就删除下标位，默认为最后一个元素
# print(names)
# # print(names.index("zhangyang"))
# # print(names[names.index("zhangyang")])
# print(names.count("zhangyang"))
# # names.clear()
# # print(names)
# names.reverse()
# print(names)
# names.sort()
# print(names)
# names2=[1,2,3,4]
# names.extend(names2)
# print(names)
# del names2
# print(names.names2)
names=["4zhangyang","guyun","#!xiangpeng","Xchengronghua","zhangyang",["alex","jack"],"xuliangchen"]

# names2=copy.deepcopy(names)
# print(names)
# print(names2)
# # print(names)
# # print(names2)
# # names[3]="向鹏"
# # print(names)
# # print(names2)
# names[2]="向鹏"
# names[5][0]="alexddd"
# print(names)
# print(names2)
for i in names:
    print(i)
print(names[::2])
print(names[:])

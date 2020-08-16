# #!/usr/bin/env python3
# #__author__="dlj"
# #data = open("day2/yesterday",encoding="utf-8").read()
# f = open("day2/yesterday2", 'a', encoding="utf-8")  #文件句柄
# #a=append追加
# f.write("\nwhen i was young i listen to the radio\n")
# data = f.read()
# print('---read',data)
# f.close()
#f = open("day2/yesterday",'r', encoding="utf-8")
# for i in range(5):
#     print(f.readline())
# print(f.readlines())
# low loop
# for index, line in enumerate(f.readlines()):
#     if index == 9:
#         print('------我是分割线------')
#         continue
#     print(line.strip())
# high bigger
# count=0
# for line in f:
#     if count == 9:
#         print('------我是分割线------')
#         count +=1
#         continue
#     print(line)
#     count += 1
# print(f.tell())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.tell())
# f.seek(10)
# print(f.readline())
# print(f.encoding)
# print(f.fileno())
# #print(f.flush())
# print(dir(f.buffer))
# f = open("day2/yesterday2", 'r+', encoding="utf-8")#文件句柄  读写
#f = open("day2/yesterday2", 'w+', encoding="utf-8")  # 文件句柄    写读
#f = open("day2/yesterday2", 'a+', encoding="utf-8")  # 文件句柄    写读
#f = open("day2/yesterday2", 'rb', encoding="utf-8")  # 文件句柄    二进制文件
# f=open("day2/yesterday2",'rb')
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f=open("day2/yesterday2",'wb')  #文件句柄，二进制文件
# f.write("hello binary\n".encode())
# f.close()
# f.write("hello 1\n")
# f.flush()#强制刷新，将内存中的文件写入硬盘
# f.write("hello 2\n")
# f.truncate(20)#从头开始截断
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.tell())
# f.write("-------------diao---------\n")
# f.write("-------------diao---------\n")
# f.write("-------------diao---------\n")
# f.write("-------------diao---------\n")
# f.seek(10)
# print(f.readline())
# f.write("should be at the begining of the second line")
# f.close()

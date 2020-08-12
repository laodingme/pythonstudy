# #!/usr/bin/env python3
# #__author__="dlj"
# #data = open("day2/yesterday",encoding="utf-8").read()
# f = open("day2/yesterday2", 'a', encoding="utf-8")  #文件句柄
# #a=append追加
# f.write("\nwhen i was young i listen to the radio\n")
# data = f.read()
# print('---read',data)
# f.close()
f = open("day2/yesterday",'r', encoding="utf-8")
# for i in range(5):
#     print(f.readline())
#print(f.readlines())
#low loop
# for index, line in enumerate(f.readlines()):
#     if index == 9:
#         print('------我是分割线------')
#         continue
#     print(line.strip())
#high bigger
# count=0
# for line in f:
#     if count == 9:
#         print('------我是分割线------')
#         count +=1
#         continue
#     print(line)
#     count += 1
print(f.tell())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.tell())
f.seek(10)
print(f.readline())
print(f.encoding)

#print(f.flush())
print(dir(f.buffer))
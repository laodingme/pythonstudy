#!/usr/bin/env python3
#f = open("day2/yesterday2",'w', encoding="utf-8")  # 文件句柄
f = open("day2/yesterday2",'a', encoding="utf-8")  # 文件句柄
#a=append追加
f.write("\nwhen i was young i listen to the radio\n")
data = f.read()
print('---read',data)
f.close()
#!/usr/bin/python3.7
name = "my \tname is {name} and i am {year}  old"
print(name.capitalize())
print(name.count("a"))
print(name.casefold())
print(name.center(50,"-"))
print(name.endswith("lj"))#判断字符串以什么结尾
print(name.expandtabs(tabsize=30))#如字符串中有\t，tabsize控制空格输出
print(name.find("y"))#取字符开始的下标
print(name[name.find("name"):])
print(name.format(name='dlj',year=29))
print(name.format_map({'name':'alex','year':12}))
print(name.isalnum())
print('abc123'.isalnum())#判断字符串中是否为字母和数字
print('abC'.isalpha())#判断字符串中是否为英文字母
print('1A'.isdecimal())#判断字符串中的数字是否为十进制
print('1A'.isidentifier())#判断是不是一个合法的标识符
print('A1'.isidentifier())#判断是不是一个合法的标识符
print('33'.isnumeric())#判断字符串中是不是只有数字
print('3.3'.isnumeric())#判断字符串中是不是只有数字
print(' '.isspace())#判断是不是空格
print('My Name Is '.istitle())
print('my name is '.istitle())
print('My Name Is'.isprintable())#判断是否能打印，系统中有些文件不能打印
print('My name Is '.isupper())#判断是否全为大写
print('My Name Is'.join("=="))
print('+'.join(['1','2','3']))
print(name.ljust(50,'*'))#设置打印的字符串长度，不够长度,后面用*号补齐
print(name.rjust(50,'-'))#设置打印的字符串长度，不够长度，前面用-补齐
print('Dlj'.lower())#大写变小写
print('\nDlj\n'.lstrip())#去掉左边的回车
print('\ndlj\n'.rstrip())#去掉右边的回车换行
print('dlj')
print('\nDlj\n'.strip())#去掉两边的回车
p=str.maketrans("abcdef","123456")#将前面字符串中的字符与后面字符串中的字符一一对应

print("alex li".translate(p))
print('dlj.d'.replace('d','D',1))
print('DLj.dlj'.rfind('d'))#从右开始查找d，找到后返回下标
print('D l j . d'.split(' '))#将split中的提示符当分隔符。将字符串返回成列表
print('1+2\n+3+4'.splitlines())#将\n变为分隔符生成列表
print('DLj dlj'.swapcase())#将英文大小写互相转换
print('lex li'.title())#字母第一个字符变成大写
print('lex li'.zfill(50))#不够用填充
__author__ = "dlj"



school = "o1dboy edu."
names = ["Alex", "Jack", "Rain"]
names_tuple=(1,2,3,4)
    names[0]="老丁"#字典，列表可以在函数内直接改全局
    print("inside func",names)
change_name()
print(names)
#school = "01dboy edu."
# def change_name():
#     global name
#     name="dlj"
# def change_name(name):
#     global school #如果加了这个，那就变成全局函数，全局生效
#     school="Mage Linux"#函数内为局部变量，出了函数失效
#     print("before change", name,school)
#     name = "Dlj"  #这个函数就是这个变量的作用域
#     age=29
#     print("after change", name)

# change_name()
# print(name)

# print(school)
# name = "dlj"
# change_name(name)
# print(name)
# print(school)
# print("age",age)

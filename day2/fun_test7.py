__author__ = "dlj"
def test(x,y,z=3):
    print(x)
    print(y)

test(1, 2)
#*args:接收N个位置参数，转换成元组
def test1(*args):
    print(args)
test1(1, 2, 3, 4, 5, 6)
test1(*[1, 2, 4, 5, 6])  #*args=tuple([1,2,3,4,5])
def test2(x, *args):
    print(x)
    print(args)
test2(1, 2, 3, 4, 5, 6, 7)
def test3(**kwargs):
    print(kwargs)
    print(kwargs['name'])
    print(kwargs['age'])
    print(kwargs['sex'])
test3(name='alex', age=8, sex='F')
#**kwargs:把n个关键字参数，转换成字典的方式
test3(**{'name': 'alex', 'age': 8, 'sex': 'F'})
def test4(name, **kwargs):
    print(name)
    print(kwargs)
test4('alex', age=18, sex='m')
test4('alex', **{'age': 18, 'sex': 'm'})
def test5(name, age=18,*args,**kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)
    logger("TEST5")

test5('alex', age=34, sex='m', hobby='tesla')

def logger(source):
    print("from %s" % source)

test5('alex', age=34, sex='m', hobby='tesla')
__author__ = "dlj"
def test1():
    print('in the test1')
    
    
def test2():
    print('in the test2')
    return 0
def test3():
    print('in the test3')
    return 1,'hello',['alex','wupeiqi'],{'names':'alex'}
x = test1()
y = test2()
z = test3()
print(x)
print(y)
print(z)
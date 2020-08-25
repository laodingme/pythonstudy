__author__ = "dlj"
def test(x, y,z):
    print(x)
    print(y)
    print(z)
test(1, 2)
test(y=1, x=2)
#test(3, x=2)
#test(3,y=2,6)#不能这么写，位置参数与关键字参数最好别混写
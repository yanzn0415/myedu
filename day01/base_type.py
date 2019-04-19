def int_demo():
    print('nannan')
    print('gege')

def test1():
    print('test1')
def test2():
    print('test2')               #   方法内的代码（注释）
def test3():                     #test 起的方法名
    print('test3')              #def  声明一个方法
    # (main)  方法可以直接执行的方法

def int_nan():
    aint = 5     #  int 类型  (整数)
    print(aint)  # 打印  aint  变量
    type(aint)   # type  类型的意思     获取aint 的类型
    print(type(aint))

def str_nan():
    astr = '5'  #  str 类型  （字符串）
    print(astr)
    type(astr)
    print(type(astr))

def float_nan():  # float  小数类型
    afloat = 0.1
    print(afloat)
    type(afloat)
    print(type(afloat))

def add_nan(a,b,):  #  add 加法
    print(a+b)

def type_nannan():
    aint = 5
    print(type(aint) )
    print(type(int(aint)))
    print(type(str(aint)))

def str_join():
    a = 5
    b = '爸爸'
    c = 2.1
    print(str(a)+b+str(c))
    print('%s %s %s'%(a,b,c))  #%s 占位符

def jianfa_nan(a,b):
    c=a-b
    return c

if __name__ == '__main__':

     print('jjj')
    #int_demo()
    # test3()
    # test1()
    # test2()
    # int_nan()
    # str_nan()
    #float_nan()
    # add_nan(4,11)
    # type_nannan()
    # str_join()
    # c=jianfa_nan(7,3)
    # print(type(c))
    # print(c)
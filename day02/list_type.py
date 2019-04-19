#查询或者获取list 里面的值（元素）
#a[索引]:或者叫下值标  元素从0开始数

def list_sel(a):
    #顺序取值: 从0开始数
    print(a[2])
    #倒叙取值: 从-1 开始数
    print(a[-1])
    #切片取值 语法:前所引值: 后索引值   取值的时候取到后索引值的前一位
    print(a[1:3])
def list_del():
    alist=[2,'你好',0.1,'a']
    alist.pop()
    print(alist)
    alist.pop(0)
    print(alist)
    alist.append('hahahhahha')
    print(alist)
    blist=['wo']
    alist.append(blist)
    print(alist)
if __name__ == '__main__':
    alist=[2,'你好',0.1,'a']
    list_del()




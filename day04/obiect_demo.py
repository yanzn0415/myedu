class yan(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def tiaochuan(self):
        print('%s在跳船'%self.name)
    def shuijiao(self):
        print('%s在睡觉'%self.name)

class nan(yan):
    def gongzuo(self):
        self.tiaochuan
        print('%s在修船'%self.name)
        self.shuijiao
        print('%s没修好'%self.name)

if __name__ == '__main__':
    # nan=yan('杰克','25','男')
    # nan.tiaochuan()
    # nan.shuijiao()
    # nan.tiaochuan()
    nan=nan('杰克','25','男')
    nan.gongzuo()
    nan.shuijiao()
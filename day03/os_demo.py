import os

def test():
    pass

if __name__ == '__main__':
    # os.getcwd()  ��ȡ��ǰĿ¼
    pwd = os.getcwd()
    print(pwd)

    # �����ϼ�Ŀ¼���ַ���
    b = os.path.abspath('..')
    print(b)

    # �������ϼ�Ŀ¼���ַ���
    c = os.path.abspath('../..')
    print(c)
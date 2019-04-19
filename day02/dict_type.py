adict = {"username":"yansl","password":"123456"}
bdict = {5:"yansl","password":[2,5]}
def dict_sel():
    print(adict['username'])
    print(bdict[5])

# if __name__ == '__main__':
#     dict_sel()
def dict_del():
    adict.pop('password')
    print(adict)

def dict_add():
    adict.update(bdict)
    print(adict)
def dict_update():
    adict['username'] = '闫松林'
    print(adict)
if __name__ == '__main__':
    # dict_del()
    # dict_add()
    dict_update()
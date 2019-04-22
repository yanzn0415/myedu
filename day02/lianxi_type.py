import json
adict = {"username":"yansl","password":"123456"}
bdict = {'5':"yansl","password":[2,5]}
cdict = '{"username":"yansl","password":"123456"}'
def list_type():
    alist=['a',1,0,123]
    alist[0:-1]
    print(alist)
def adict_type():
    print(type(adict))
    ddict=json.dumps(adict)
    print(ddict)
    print(type(ddict))
def cdict_type():
    print(type(cdict))
    edict=json.loads(cdict)
    print(type(edict))
    print(edict)
if __name__ == '__main__':
    # adict_type()
    cdict_type()
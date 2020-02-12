import os

path = ''
f=os.listdir(path)
print(f[0].split('-')[-1])
# print(f[1].split('.')[0]+'-'+f[1].split('.')[5]+'.'+f[1].split('.')[-1])

n = 0
for i in f:
    oldname = path + f[n]
    newname = path + f[n].split('-')[-1]
    
    print(oldname + '=>' + newname)
    os.rename(oldname,newname)
    n = n+1
# file management system
import os
print('enter 1 to write , 2 to read , 3 to append')
action=int(input(''))
if action==1:
    a=input('enter file name')
    b=input('enter content')
    file=open(a,'w')
    file.write(b)
    file.close()
elif action==2:
    c=os.listdir()
    for i in c:
        if i.endswith('.txt'):
            print(i)
    d=input('choose and enter file')
    file=open(d,'r')
    file.seek(0)
    print(file.read())
elif action==3:
    c=os.listdir()
    for i in c:
        if i.endswith('.txt'):
            print(i)
    e=input('choose and enter append file')
    e_cont=input('enter content to append')
    file=open(e,'a+')
    file.write(e_cont)
    file.close()
else:
print('enter valid data')
            

l1=[1,2,3,4,5,6,7,8,9,10]
oddlst=[]
evenlst=[]
for i in l1:
    if(i%2==0):
        evenlst.append(i)
    else:
        oddlst.append(i)
print('even num',evenlst)
print('odd num',oddlst)
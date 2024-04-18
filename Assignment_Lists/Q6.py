list = [2,4,6,8,10]
print("before swap list", list)
size=len(list)
temp=list[0]
list[0]=list[size-1]
list[size-1]=temp
print("after swap list", list)



def check_ascending_order(list):
    return all(list[i]<=list[i+1] for i in range(len(list)-1))
l1=[4,2,1,3]
if check_ascending_order(l1):
    print('asencending order')
else:
    print('not')
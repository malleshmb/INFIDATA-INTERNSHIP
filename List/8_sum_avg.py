sum = 0
avg = 0
l1 = [2,4,6,8,10]
for i in l1:
    sum = sum + i
print('Sum of all elements of l1 is:',sum)
avg = sum/len(l1)
print("Average of l1 is:",avg)

for i in l1[:3]:
    print(i)

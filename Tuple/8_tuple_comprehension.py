t1 = ( i for i in range(1,4))
print("Tuple t1 is:",t1)

t2 = (i**2 for i in range(1,6) if i%2==0)
print("Tuple t2 is:",t2)

l1= [i for i in range(1,7)]
print("List l1 s:",l1)
t1 = tuple(l1)
print("Tuple t1 is:",t1)
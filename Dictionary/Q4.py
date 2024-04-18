dict1 = {'x': 10, 'y': 8}
dict2 = {'a': 6, 'b': 4}

def Merge(dict1, dict2):
    for i in dict2.keys():
        dict1[i] = dict2[i]
    return dict1

dict3 = Merge(dict1, dict2)
print(dict3)

marks={}.fromkeys(['python','java','web'],100)
print(marks)


for i in marks.items():
    print(i)

print(marks.keys())
print(marks.values())

print(sorted(marks))
print(sorted(marks,reverse=True))

print(sorted(marks.items()))
print(sorted(marks.items(),reverse=True))
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
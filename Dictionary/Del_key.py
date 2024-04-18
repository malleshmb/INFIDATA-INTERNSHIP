student = {
    "Name": "Arun",
    "Id": 101,
    "Branch": 'CS',
    "Age": 20,
    "Gender": "male",
    "City": "Bangalore"
}
print("Before Delete :", student)
# Keys to remove From a Dict
keys = ["Gender", "City"]

for k in keys:
    student.pop(k)
print("After Delete :", student)


list = ['a','b','a','c','d','c','c']
frequency = {}
for item in list:
   if (item in frequency):
      frequency[item] += 1
   else:
      frequency[item] = 1
for key, value in frequency.items():
   print("% s -> % d"%(key,value))
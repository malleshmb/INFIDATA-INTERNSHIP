l1 = [6,7,8,9]
print("l1[2]:",l1[2])
try:
    print("l1[2]:",l1[2])
    print("l1[5]:",l1[5])
except ZeroDivisionError as e:
    print("You have trying to divide and integer number by zero")
    print("e value is:")
finally:
    print("am at finally block:")
    print("Execution at finally")
print("End")

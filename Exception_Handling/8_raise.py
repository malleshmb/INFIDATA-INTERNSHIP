print("raise keyword demo")
try:
    raise ZeroDivisionError("demo message")
except ZeroDivisionError as e:
    print("am at ZeroDividionError xcept block")#raise is used for to give explicit call to except block
    print("e value is",e)
print("End")
earth_weight = float(input("Enter your weight on Earth (in lbs): "))
planet = int(input("Enter the number of the planet you want to fight on: "))

if planet == 1:
    target_weight = earth_weight * 0.78
elif planet == 2:
    target_weight = earth_weight * 0.39
elif planet == 3:
    target_weight = earth_weight * 2.65
elif planet == 4:
    target_weight = earth_weight * 1.17
elif planet == 5:
    target_weight = earth_weight * 1.05
elif planet == 6:
    target_weight = earth_weight * 1.23
else:
    print("Invalid planet number entered.")
    target_weight = None
if target_weight is not None:
    print("Your weight on the destination planet will be: {:.2f} lbs ".format(target_weight))
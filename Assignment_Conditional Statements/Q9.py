age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ").upper()
days = int(input("Enter number of days: "))

if age >= 18 and age <= 40:
    if gender == 'M':
        if age < 30:
            wages = 700 * days
        else:
            wages = 800 * days
    elif gender == 'F':
        if age < 30:
            wages = 750 * days
        else:
            wages = 850 * days
    print("Wages: $", wages)
else:
    print("Invalid input")
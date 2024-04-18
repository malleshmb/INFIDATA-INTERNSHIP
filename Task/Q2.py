gender = input("Enter your gender (male/female): ")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))

if gender.lower() == "female":
    if age >= 20:
        married = input("Are you married? (yes/no): ")
        if married.lower() == "yes":
            print("Mrs. " + first_name + " " + last_name)
        else:
            print("Ms. " + first_name + " " + last_name)
    else:
        print(first_name + " " + last_name)
elif gender.lower() == "male":
    if age >= 20:
        print("Mr. " + first_name + " " + last_name)
    else:
        print(first_name + " " + last_name)
else:
    print("Invalid gender entered.")
married = input("Are you married? (yes/no)")
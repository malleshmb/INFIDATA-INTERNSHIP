salary = float(input("Enter your salary: "))
years_of_service = int(input("Enter your years of service: "))
if years_of_service > 10:
    bonus_percentage = 0.10
elif 6 <= years_of_service <= 10:
    bonus_percentage = 0.08
else:
    bonus_percentage = 0.05
bonus_amount = salary * bonus_percentage
print(f"Your bonus amount is: {bonus_amount:.2f}")
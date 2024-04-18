Ename=(input("enter the Ename"))
Eid=int(input("enter the Eid"))
Basic_salary=int(input("enter the Basic_salary"))
DA=(Basic_salary*40)/100
HRA=(Basic_salary*20)/100
Gross_salary=Basic_salary+DA+HRA
print("DA 40% of Basic salary",DA)
print("HRA 20% of Basic salary",HRA)
print("Gross salary",Gross_salary)
print("vasanth Internation [p]ltd")
print("No.15,Nagapara Dist,Bangolore")
print("------------------------------")
print("Employee Payroll System")
print("---------------------------")
Id=int(input("Enter the Employee Id:"))
Name=input("Enter the Employee Name:")
Salary=int(input("Enter the Salary:"))
print("Income")
Bonas=Salary*20/100
print("Bonas(20 percentage):",Bonas)
Overtime=Salary*10/100
print("Overtime(10 percentage):",Overtime)
TravelAllvance=Salary*5/100
print("Travelallvance(5 percentage):",TravelAllvance)
Grass=Salary+Bonas+Overtime+TravelAllvance
print("Grass paid in Rupees:",Grass)

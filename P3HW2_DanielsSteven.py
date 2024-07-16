# Steven Daniels
# 7-9-2024
# P3HW2
# This program will calculate an employee's pay

name = input("Enter the employee's name: ")
hoursWorked = float(input("Enter number of hours worked: "))
payRate = float(input("Enter employee's pay rate: "))

if hoursWorked > 40:
    # calculate overtime
    overtimeHours = hoursWorked - 40
    # calculate overtime pay
    overtimePay = overtimeHours * (payRate * 1.5)
    # calculate pay for regular hours
    regPay = 40 * payRate
    # calculate gross pay
    grossPay = regPay + overtimePay

else:
    # set overtime hours and pay to zero
    overtimePay = 0
    overtimeHours = 0
    regPay = payRate * hoursWorked
    grossPay = regPay 

print("-" * 37)
print("Employee name: ",name,"\n")
print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"Overtime":<12}{"Overtime Pay":<20}{"RegHour Pay":<15}{"Gross Pay"}')
print("-" * 100)

print(f'{hoursWorked:<15}{payRate:<12}{overtimeHours:<12}{overtimePay:<20.2f}{"$"}{regPay:<20.2f}{grossPay:.2f}')


    

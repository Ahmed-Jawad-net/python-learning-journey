#Monthly Salary Calculation
hourly_rate = float(input("Enter you hourly job rate: "))
hours_worked = float(input("Enter the number of hours you worked in a month: "))
monthly_salary = hourly_rate * hours_worked
print(f"Your monthly salary is: {monthly_salary:.2f}")
yearly_salary = monthly_salary * 12
print(f"Your yearly salary would be: {yearly_salary:.2f}")

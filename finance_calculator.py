monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

annual_savings = monthly_savings * 12 + (monthly_savings * 12 *0.05)

print(f"Your monthly savings: ${int(monthly_savings)}")
print(f"Projected annual savings after interest: ${int(annual_savings)}")
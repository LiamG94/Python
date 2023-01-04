monthly_income = 2000
weekly_rent = 300
monthly_bills = 220
weekly_savings_deposit = 50
weekly_expenses = 80
total_expenses = (weekly_rent + weekly_expenses + weekly_savings_deposit)*4 + monthly_bills
print("My total expenses for a month equates to €{}".format(total_expenses))
leftover_funds = monthly_income - total_expenses
print("When I subtract this from my monthly income of €{} I have €{} left over, which I keep for emergencies.".format(monthly_income,leftover_funds))